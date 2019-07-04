import os
import time
import urllib
import json
import logging
import psutil
import threading
from queue import Queue
from threading import Thread
from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display
from urllib.request import Request, urlopen
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


GECKODRIVER = "geckodriver"

class WebDriverUtils:
    """
    This class is responsible for all webdriver related functionality
    """
    
    GEKO_EXECUTABLE_PATH = './resources/geckodriver'
    URL = "http://www.google.co.in/search?q={}&source=lnms&tbm=isch"
    SHOW_MORE_BUTTON_ID = 'smb'
    

    def __init__(self):
        self.display = Display(visible=0, size=[800, 600])
        self.display.start()
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        self.driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=self.GEKO_EXECUTABLE_PATH)

    def close(self):
        print('closeing')
        self.display.stop()
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == GECKODRIVER:
                proc.kill()

    def get_image_urls_from_google_images(self, search_term):
        self.load_google_image_search_page(search_term)
        last_height = self.get_scroll_height() #.execute_script("return document.body.scrollHeight")
        actual_images = []
        flg = 0
        while True:
            # Action scroll down
            print('scroll down')
            self.scroll_to_bottom() #.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print('pageScrolled')
            new_height = self.get_scroll_height() #.execute_script("return document.body.scrollHeight")
            print('New Height : ' + str(new_height))
            if new_height == last_height:
                if flg == 0:
                    self.click_show_more_buttom() #.find_element_by_id('smb').click()
                    flg = 1
                else:
                    break
                time.sleep(1)
            last_height = new_height
        actual_images = self.get_image_urls()
        return actual_images


    def get_image_urls(self) :
        soup = BeautifulSoup(self.driver.page_source , 'html.parser')
        actual_images = []# contains the link for Large original images, type of  image
        for a in soup.find_all("div",{"class":"rg_meta"}):
            link , Type = json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
            actual_images.append((link,Type))
        return actual_images

    def isPageLoaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def get_page_source(self):
        return self.driver

    def load_url(self, url):
        self.driver.get(url)

    def load_google_image_search_page(self, search_term):
        self.load_url(self.URL.format(search_term))
        while not self.isPageLoaded(): pass
    
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_scroll_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def click_element(self, element_id):
        self.driver.find_element_by_id(element_id).click()

    def click_show_more_buttom(self):
        self.click_element(self.SHOW_MORE_BUTTON_ID)

class DownloadUtils:

    ERROR_IMAGE = './resources/no-image-icon.jpg'

    def __init__(self):
        self.num_prefetch_threads = 10
        self.current_image_index = -1
        self.image_tuple_list = []
        self.prefetched_images_dict = {}
        self.saved_images_dict = {}
        self.prefetch_url_queue = Queue()
        self.first_load = True
        for i in range(self.num_prefetch_threads):
            worker = Thread(target=self.download_image_from_url)
            worker.setDaemon(True)
            worker.start()

    def download_image_from_url(self):
        while True:
            print('Looking for the next url')
            img_url, _ = self.prefetch_url_queue.get()
            print('Downloading:' + img_url)
            # instead of really downloading the URL,
            # we just pretend and sleep
            try:
                raw_img = urllib.request.urlopen(img_url,timeout=1000)
                raw_img = raw_img.read()
            except:
                with open(self.ERROR_IMAGE, 'rb') as image_file:
                    image = image_file.read()
                raw_img = image
            self.prefetched_images_dict[img_url] = raw_img
            self.prefetch_url_queue.task_done()

    def get_next_image(self):
        url , _ = self.image_tuple_list[self.current_image_index + 1]
        if url in self.saved_images_dict:
            image_filename = self.saved_images_dict.get(url)
            raw_image = self.get_image_from_file(image_filename)
        else:
            raw_image = self.prefetched_images_dict.get(url)
        if raw_image:
            print('Here')
            self.current_image_index += 1
            if self.current_image_index == 8:
                self.save_current_image('.')
            prefetch_url = self.image_tuple_list[self.current_image_index + self.num_prefetch_threads]
            if not prefetch_url in self.prefetched_images_dict:
                self.prefetch_url_queue.put(prefetch_url)
                self.prefetched_images_dict[prefetch_url] = None
        return raw_image

    def get_previous_image(self):
        if self.current_image_index:
            self.current_image_index -= 1
        url , _ = self.image_tuple_list[self.current_image_index]
        if url in self.saved_images_dict:
            image_filename = self.saved_images_dict.get(url)
            raw_image = self.get_image_from_file(image_filename)
        else:
            raw_image = self.prefetched_images_dict.get(url)
            print('Get from Queue')
        return raw_image

    def get_image_from_file(self, image_filename):
        with open(image_filename, "rb") as image_file:
            f = image_file.read()
            raw_image = bytearray(f)
        return raw_image

    def delete_current_image(self):
        image_filename = self.saved_images_dict.pop(self.image_tuple_list[self.current_image_index]) 
        os.remove(image_filename)
        return image_filename

    def get_current_image_index(self):
        return self.current_image_index + 1

    def get_url_count(self):
        return len(self.image_tuple_list)

    def get_saved_images_count(self):
        return len(self.saved_images_dict)
    
    def update_url_list(self, url_list):
        self.image_tuple_list = self.image_tuple_list + url_list 
        if self.first_load:
            for i in range(1,self.num_prefetch_threads+1):
                self.prefetch_url_queue.put(self.image_tuple_list[self.current_image_index+i])
                self.prefetched_images_dict[self.image_tuple_list[self.current_image_index+i]] = None
            self.first_load = False

    def save_current_image(self,save_dir):
        current_image = self.image_tuple_list[self.current_image_index]
        img_type = current_image[1]
        img_url = current_image[0]
        saved_filename = ''
        if img_url in self.prefetched_images_dict:
            print("Saving Image to {} \nType: {}\t URL: {}".format(save_dir,img_type,img_url))
            raw_image = self.prefetched_images_dict.pop(img_url)
            saved_filename = os.path.join(save_dir , "img_" + str(int(time.time()))+"."+img_type)
            with open(saved_filename, 'wb') as image_file:
                image_file.write(raw_image)
            self.saved_images_dict[img_url] = saved_filename
        else:
            print('Image Not Prefetched')
        return saved_filename

    # class ThreadFunc(threading.Thread):
    #     def __init__(self, target, *args):
    #         self._target = target
    #         self._args = args
    #         threading.Thread.__init__(self)
     
    #     def run(self):
    #         self._target(*self._args)

def main(args):
    pause = 5
    save_directory = args.save_dir
    driver = WebDriverUtils()
    actual_images = driver.get_image_urls_from_google_images(args.num_images, args.search_term)
    print(len(actual_images))
    count = 0
    for img_url , file_type in actual_images:
        count += 1
        logging.debug("count : " + str(count) + "\tType : " + file_type)
        try:
            raw_img = urllib.request.urlopen(img_url,timeout=1000)
            raw_img = raw_img.read()
            
        except Exception as e:
            logging.exception("could not load : " + img_url)
    

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--search_term', type=str, default='trees', help='Search term for images')
    parser.add_argument('--url_file', type=str, help='Path(s) of the url file')
    parser.add_argument('--save_dir', type=str, default='./', help='Path of the directory to save images')
    parser.add_argument('--num_images', type=int, default='600', help='Number of images to load from google')
    return parser.parse_args(argv)

if __name__ == '__main__':
    import argparse
    main(parse_arguments(sys.argv[1:]))