# scrape from https://automated.pythonanywhere.com

from selenium import webdriver

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
    driver.get('https://automated.pythonanywhere.com')
    return driver

def clean_text(text):
    """Extract only the number from text"""
    output = text.split(":")
    return output

def main():
    driver = get_driver()
    #element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[1]')
    number = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
    output =  clean_text(number.text)
    return output

print(main())