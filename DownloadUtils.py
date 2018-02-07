import os
import time
import urllib
import json
import logging
import psutil
import threading
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
    
    GEKO_EXECUTABLE_PATH = './geckodriver'
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

    def __init__(self):
        self.is_download_complete = True
        self.is_save_complete = True

    def download_image_from_url(self,img_url):
        raw_img = urllib.request.urlopen(img_url,timeout=1000)
        raw_img = raw_img.read()
        return raw_img


    def save_current_image(self,save_dir,raw_img,img_type):
        filename = "img" + "_"+ str(int(time.time()))+"."+img_type
        f = open(os.path.join(save_dir , filename), 'wb')
        f.write(raw_img)
        f.close()
        return filename

    class ThreadFunc(threading.Thread):
        def __init__(self, target, *args):
            self._target = target
            self._args = args
            threading.Thread.__init__(self)
     
        def run(self):
            self._target(*self._args)

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