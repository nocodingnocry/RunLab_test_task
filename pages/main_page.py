import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
class Main_page(Base):

    url = 'https://www.runlab.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    locator_to_shoes = '/html/body/div[1]/div[2]/footer/div/div[1]/div[1]/ul/li[1]/a'
    locator_accept_cookie = '//*[@id="site-content"]/div[15]/button'

    # Getters

    def get_shoes_section(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.locator_to_shoes)))

    def get_accept_cookie(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.locator_accept_cookie)))

    # Actions

    def scroll_to_down(self):
        self.get_shoes_section().location_once_scrolled_into_view
        print('Scrolled to shoe`s icon')
    def click_on_shoes_page(self):
        self.get_shoes_section().click()
        print('Clicked to section Shoes')

    def click_to_accept_cookie(self):
        self.get_accept_cookie().click()
        print('Cookie was accepted')

        # Methods

    def move_to_shoes_section(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_to_accept_cookie()
        self.scroll_to_down()
        self.click_on_shoes_page()
        time.sleep(5)