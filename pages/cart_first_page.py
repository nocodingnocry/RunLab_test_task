import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.loger import Logger


class Cart_page_1(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators

    locator_make_order = '//*[@id="js-wrapper-basket"]/div[2]/div/div[5]/a'

#Gettings
    def get_make_order(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_make_order)))

#Actions

    def click_to_make_order(self):
        self.get_make_order().click()
        print('Clicked to button "Make an order"')


#Methods

    def move_to_second_step_order(self):
        with allure.step('Move_to_second_step_order'):
            Logger.add_start_step(method='move_to_second_step_order')
            self.click_to_make_order()
            Logger.add_end_step(url=self.driver.current_url, method='move_to_second_step_order')

