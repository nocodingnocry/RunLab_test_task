import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.loger import Logger

class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    locator_email_field = '//*[@id="user-login"]'
    locator_password_field = '//*[@id="user-password"]'
    locator_login_button = '//*[@id="form-login_submit"]'

    # Getters
    def get_email_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.locator_email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.locator_password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.locator_login_button)))

    # Actions

    def input_email(self):
        self.get_email_field().send_keys('luchkin1997@mail.ru')
        print('Writed email on email field')

    def input_password(self):
        self.get_password_field().send_keys('AutomationQA')
        print('Writed password on password field')

    def click_login_button(self):
        self.get_login_button().click()
        print('Clicked to login Button')

    # Methods

    def auth(self):
        with allure.step('Input email and password, click Login button'):
            self.input_email()
            self.input_password()
            self.click_login_button()
            Logger.add_end_step(url=self.driver.current_url, method='auth')


