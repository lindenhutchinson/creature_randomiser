from selenium import webdriver
import time
import sys


SLEEP_TIME = 2
SEL_RETRIES = 3

class Scraper:
    def __init__(self, url, driver_dir):
        self.driver = self.make_web_driver(url, driver_dir)

    def quit(self):
        self.driver.close()

    def make_web_driver(self, url, driver_dir):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized');
        chrome_options.add_argument('--start-fullscreen');
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--enable-javascript")
        driver = webdriver.Chrome(
            options=chrome_options, executable_path=driver_dir)
        
        driver.get(url)
        return driver
    
    def try_get_ele_by_id(self, id):
        count = 0
        while(count != SEL_RETRIES):
            try:
                return self.driver.find_element_by_id(id)
            except:
                count+=1
                print("Attempt {}. Couldn't find {}. Will retry in {} seconds".format(count,id,SLEEP_TIME))
                time.sleep(SLEEP_TIME)


        print("Couldn't find {} after max retries. Quitting...".format(id))
        sys.exit(0)

    def try_get_ele_by_xpath(self, xpath):
        count = 0
        while(count != SEL_RETRIES):
            try:
                return self.driver.find_element_by_xpath(xpath)
            except:
                count+=1
                print("Attempt {}. Couldn't find {}. Will retry in {} seconds".format(count,xpath,SLEEP_TIME))
                time.sleep(SLEEP_TIME)


        print("Couldn't find {} after max retries. Quitting...".format(xpath))
        sys.exit(0)

    def try_get_ele_by_class_name(self, name):
        count = 0
        while(count != SEL_RETRIES):
            try:
                return self.driver.find_element_by_class_name(name)
            except:
                count+=1
                print("Attempt {}. Couldn't find {}. Will retry in {} seconds".format(count,name,SLEEP_TIME))
                time.sleep(SLEEP_TIME)


        print("Couldn't find {} after max retries. Quitting...".format(name))
        sys.exit(0)

    def get_text_by_id(self, id):
        ele = self.try_get_ele_by_id(id)
        return ele.get_attribute('innerHTML')

    def get_text_by_class(self, name):
        ele = self.try_get_ele_by_class_name(name)
        return ele.get_attribute('innerHTML')

    def click_on_xpath(self, xpath):
        ele = self.try_get_ele_by_xpath(xpath)
        ele.click()
