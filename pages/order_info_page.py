import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Order_info_class(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    locator_order_completed = '//*[@id="content"]/div[2]/div/p[1]'

    # Getters
    def get_order_completed(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_order_completed)))

    # Actions
    def read_order_completed(self):
        return self.get_order_completed().text
    # Methods

    def finish_screen(self):
        self.assert_word(self.read_order_completed(), 'Ваш заказ принят')
        self.assert_url('https://www.runlab.ru/order_third_step/')
        self.get_screenshot()

