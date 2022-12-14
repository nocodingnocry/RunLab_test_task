import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from base.base_class import Base
from utilities.loger import Logger


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locatrors
    locator_choice_size = '//*[@id="pre-buy-size-choice-popup"]/div/div[2]/a[1]'
    locator_add_to_cart = '//*[@id="content"]/div[2]/div[2]/div[2]/div[2]/a[1]'
    locator_move_to_cart = '//*[@id="move-to-basket-popup"]/div/a[2]'
    sel_css = '.add-through-popup-basket'
    #Gettings
    def get_choice_size(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_choice_size)))


    def get_add_to_cart(self):
        # result = False
        # i = 0
        #
        # while i < 2:
        #     try:
        #         self.driver.find_element(By.XPATH, self.locator_add_to_cart)
        #         result = True
        #         break
        #     except StaleElementReferenceException:
        #         i += 1

        #return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_add_to_cart)))

        return self.driver.find_element(By.XPATH, self.locator_add_to_cart)

    def get_move_to_cart(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_move_to_cart)))

    #Actions
    def click_to_size_product(self):
        self.get_choice_size().click()
        print("Size was choiced")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print('Button "add to cart" was clicked')

    def click_move_to_cart(self):
        self.get_move_to_cart().click()
        print("Moved to cart")

    # Methods

    def add_shoes_to_cart(self):
        with allure.step('Add shoes to cart'):
            Logger.add_start_step(method='add_shoes_to_cart')
            self.click_add_to_cart()
            self.click_to_size_product()
            self.click_move_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method='add_shoes_to_cart')
