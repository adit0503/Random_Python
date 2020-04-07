from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):

        path_to_chromedriver = '/home/spc/Desktop/random_python/Tinder/chromedriver' # change path as needed
        self.driver = webdriver.Chrome(executable_path = path_to_chromedriver)

    def login(self):
        self.driver.get('https://tinder.com/')

        sleep(2)
        try:
            cookies = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/button')
            cookies.click()
        except Exception:
            print('no cookies window')

        sleep(2)
        close_login_pop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button')
        close_login_pop.click()

        # fb_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
        # fb_button.click()

bot = TinderBot()
bot.login()
