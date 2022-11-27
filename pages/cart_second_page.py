import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.loger import Logger


class Cart_page_2(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    locator_last_name_field = '//*[@id="Order_name"]'
    locator_first_name_field = '//*[@id="Order_lastname"]'
    locator_second_name_field = '//*[@id="Order_patronimic"]'
    locator_phone_field = '//*[@id="Order_phone"]'
    locator_email_field = '//*[@id="Order_email"]'
    locator_checkbox_mailing = '//*[@id="yw0"]/fieldset[1]/div[6]/div/div/span'
    locator_comment_field = '//*[@id="Order_comment"]'
    locator_radio_delivery_spb = '//*[@id="Order_delivery"]/div[2]/span'
    locator_address_field = '//*[@id="Order_address"]'
    locator_make_an_order = '//*[@id="yw0_submit"]'
    locator_payment_cash = '//*[@id="Order_payment_id"]/div[1]/span'

    alert_empty_first_name = '//*[@id="Order_name_em_"]'
    alert_empty_last_name  = '//*[@id="Order_lastname_em_"]'
    alert_empty_phone_number = '//*[@id="Order_phone_em_"]'
    alert_empty_email = '//*[@id="Order_email_em_"]'
    alert_empty_delivery = '//*[@id="Order_delivery_id_em_"]'
    alert_empty_payment = '//*[@id="Order_payment_id_em_"]'

    # Getting

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 5).until(
             EC.element_to_be_clickable((By.XPATH, self.locator_first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_last_name_field)))

    def get_second_name_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_second_name_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_phone_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_email_field)))

    def get_comment_field(self):
        return WebDriverWait(self.driver, 5).until(
             EC.element_to_be_clickable((By.XPATH, self.locator_comment_field)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_address_field)))

    def get_checkbox_mailing(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_checkbox_mailing)))

    def get_radio_delivery_spb(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_radio_delivery_spb)))

    def get_button_ordering(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_make_an_order)))

    def get_payment_cash(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_payment_cash)))

    #Getters for Alert checks

    def get_alert_empty_fist_name(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.alert_empty_first_name)))

    def get_alert_empty_last_name(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.alert_empty_last_name)))

    def get_alert_empty_phone_number(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.alert_empty_phone_number)))

    def get_alert_empty_email(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.alert_empty_email)))

    def get_alert_empty_delivery(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.alert_empty_delivery)))

    def get_alert_empty_payment(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.alert_empty_payment)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name_field().send_keys(first_name)
        print(f'input first_name: {first_name}')

    def input_last_name(self, last_name):
        self.get_last_name_field().send_keys(last_name)
        print(f'input last_name: {last_name}')

    def input_second_name(self, second_name):
        self.get_second_name_field().send_keys(second_name)
        print(f'input second_name: {second_name}')

    def input_phone_number(self, phone_number):
        self.get_phone_field().send_keys(phone_number)
        print(f'input phone: {phone_number}')

    def input_email(self, email):
        self.get_email_field().send_keys(email)
        print(f'input email: {email}')

    def click_mailing_checkbox(self):
        self.get_checkbox_mailing().click()
        print(f'checkbox off')

    def click_delivery_button_spb(self):
        self.get_radio_delivery_spb().click()
        print('Choiced delivery in Saint-Petersburg')

    def input_address_field(self, address):
        self.get_address_field().send_keys(address)
        print(f'input addres: {address}')

    def input_comment(self, comment):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_comment_field())
        self.get_comment_field().send_keys(comment)
        print(f'input comment: {comment}')

    def click_to_make_order(self):
        self.get_button_ordering().click()
        print('Order completed')

    def click_payment_cash(self):
        self.get_payment_cash().click()
        print('Type of payment was choice')

    #Alert Actions

    def read_alert_empty_first_name(self):
        print(f'first_name_alert:{self.get_alert_empty_fist_name().text}')
        return self.get_alert_empty_fist_name().text

    def read_alert_empty_last_name(self):
        print(f'last_name_alert:{self.get_alert_empty_last_name().text}')
        return self.get_alert_empty_last_name().text

    def read_alert_empty_phone_number(self):
        print(f'phone_number_alert:{self.get_alert_empty_phone_number().text}')
        return self.get_alert_empty_phone_number().text

    def read_alert_empty_email(self):
        print(f'email_alert:{self.get_alert_empty_email().text}')
        return self.get_alert_empty_email().text

    def read_alert_empty_delivery(self):
        print(f'email_alert:{self.get_alert_empty_delivery().text}')
        return self.get_alert_empty_delivery().text

    def read_alert_empty_payment(self):
        print(f'email_alert:{self.get_alert_empty_payment().text}')
        return self.get_alert_empty_payment().text

    # Methods

    def completion_ordering(self):
        Logger.add_start_step(method='completion_ordering')
        self.input_first_name('Test')
        self.input_last_name('Test')
        self.input_second_name('Test')
        self.input_phone_number('79000000000')
        self.click_delivery_button_spb()
        self.input_address_field('city Etodar, street Beg 159 - 59')
        self.click_payment_cash()
        self.input_email('test@test.test')
        self.click_mailing_checkbox()
        self.input_comment('Test order')
        self.click_to_make_order()
        time.sleep(5)
        Logger.add_end_step(url=self.driver.current_url, method='completion_ordering')

    def request_alert_on_second_cart_page(self):
        Logger.add_start_step(method='request_alert_on_second_cart_page')
        self.click_to_make_order()
        self. assert_word('Необходимо заполнить поле «Фамилия».', self.read_alert_empty_last_name())
        self.assert_word('Необходимо заполнить поле «Имя».',self.read_alert_empty_first_name())
        self.assert_word('Необходимо заполнить поле «Телефон».', self.read_alert_empty_phone_number())
        self.assert_word('Необходимо заполнить поле «Эл. почта».', self.read_alert_empty_email())
        self.assert_word('Необходимо заполнить поле «Способ доставки».', self.read_alert_empty_delivery())
        self.assert_word('Необходимо заполнить поле «Способ оплаты».', self.read_alert_empty_payment())
        print('request_alert_on_second_cart_page was complited')
        #time.sleep(5)
        Logger.add_end_step(url=self.driver.current_url, method='request_alert_on_second_cart_page')







