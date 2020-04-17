import sys, os, re, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from twilio.rest import Client

# amazon credentials
amazon_username = "first.last@email.com"
amazon_password = "secret_password"

# twilio configuration
# to_mobilenumber = "+18888888888"
# from_mobilenumber = "+19999999999"
# account_sid = "fake_account_sid"
# auth_token = "fake_auth_token"
# client = Client(account_sid, auth_token)

def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome('/home/spc/Desktop/random_python/Tinder/chromedriver', chrome_options=chrome_options)
    return driver

def terminate(driver):
    driver.quit()

def check_slots():
    try:
        print('Creating Chrome Driver ...')
        driver = create_driver()

    except Exception as e:
        terminate(driver)
        raise ValueError(str(e))

if __name__ == "__main__":
    check_slots()
