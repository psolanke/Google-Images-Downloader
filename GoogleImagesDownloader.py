import sys
import os
import time
import argparse
import urllib
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

URL = "http://www.google.co.in/search?q={}&source=lnms&tbm=isch"

def getImageUrls(html_text) :
    soup = BeautifulSoup(html_text, 'html.parser')
    actualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        actualImages.append((link,Type))
    return actualImages

def isPageLoaded(driver):
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'

def main(args):
    pause = 5
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path='./geckodriver')
    driver.get(URL.format(args.search_term))
    
    while not isPageLoaded(driver): pass
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    flg = 0
    while True:
        # Action scroll down
        actualImages = getImageUrls(driver.page_source)
        if len(actualImages) > args.num_images:
            break;
        print('scroll down')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print('pageScrolled')
        newHeight = driver.execute_script("return document.body.scrollHeight")
        print('New Height : ' + str(newHeight))
        if newHeight == lastHeight:
            if flg == 0:
                driver.find_element_by_id('smb').click()
                flg = 1
            else:
                break
            time.sleep(1)
        lastHeight = newHeight
    actualImages = getImageUrls(driver.page_source)
    print(len(actualImages))
    

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--search_term', type=str, default='trees', help='Search term for images')
    parser.add_argument('--url_file', type=str, help='Path(s) of the url file')
    parser.add_argument('--save_dir', type=str, default='./', help='Path of the directory to save images')
    parser.add_argument('--num_images', type=int, default='300', help='Number of images to load from google')
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))