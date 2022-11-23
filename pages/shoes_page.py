import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Shoes_page():

    def __init__(self, driver):
        self.driver = driver

    #Locators

    locator_brands = '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div/form/div/div[2]/div[1]/span[2]'
    locator_hoka = '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div/form/div/div[2]/div[2]/ul/li[4]/a'
    locator_slider_price = '//*[@id="filter-price-slider"]/span[1]'
    locator_slider_target = '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div/form/div/div[3]/div[2]/div[1]/span[1]'
    locator_add_cart = '//*[@id="product_list"]/div[2]/div[2]/div[4]/a'
    locator_show = '//*[@id="filter-tooltip-button"]'
    locator_size = '//*[@id="pre-buy-size-choice-popup"]'
    locator_move_to_cart = '//*[@id="move-to-basket-popup"]'
    locator_item_hoka = '//*[@id="product_list"]/div[2]/div[2]/a[1]'

    # // *[ @ id = "product_list"] / div[2] / div[2] / div[3] / div[4] / a
    # // *[ @ id = "product_list"] / div[2] / div[2] / div[4] / a

    #Getters

    def get_slider_price(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_slider_price)))

    def get_add_cart(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_add_cart)))

    def get_brands_list(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_brands)))

    def get_hoka(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_hoka)))

    def get_shows(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_show)))

    def get_size(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_size)))

    def get_move_to_cart(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_move_to_cart)))

    def get_item_hoka(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.locator_item_hoka)))

    #Actions

    def choice_brand(self):
        self.get_brands_list().click()
        self.get_hoka().click()
    def change_price_on_slider(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.get_slider_price(), 20, 0)
        action.perform()
        print("Change price on slider is completed")
        self.get_shows().click()

    def scroll_to_adding(self):
        # action = ActionChains(self.driver)
        # action.move_to_element(self.get_add_cart()).perform()
        # self.get_add_cart().location_once_scrolled_into_view
        self.driver.execute_script("window.scrollTo(0, 150)")

    # def move_to_item(self):
    #     self.get_add_cart().click()
    #     print("Clicked to add shoes in cart")

    def move_to_item_hoka(self):
        self.get_item_hoka().click()

    #Methods
    def setting_filtres(self):
        self.choice_brand()
        self.change_price_on_slider()

    def open_item_product(self):
        self.scroll_to_adding()
        # self.move_to_item()
        self.move_to_item_hoka()





