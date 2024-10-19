# scrape from https://automated.pythonanywhere.com

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    #set options to make sure that the browser doesn't throw any errors
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized') #maximize the window
    options.add_argument('disable-dev-shm-usage') #disable shared memory usage
    options.add_argument('no-sandbox') #disable sandboxing
    options.add_experimental_option('excludeSwitches', ['enable-automation']) #disable automation
    options.add_argument('disable-blink-features=AutomationControlled') #disable automation

    driver = webdriver.Chrome(options=options)
    driver.get('https://automated.pythonanywhere.com/login/')
    return driver

def clean_text(text):
    """Extract only the number from text"""
    output = text.split(":")
    return output

def main():
    driver = get_driver()
    driver.find_element(by='id', value='id_username').send_keys('automated')
    time.sleep(2)
    driver.find_element(by='id', value='id_password').send_keys('automatedautomated' + Keys.RETURN)
    #driver.find_element(by='css selector', value='button').click()
    time.sleep(4)
   

print(main())