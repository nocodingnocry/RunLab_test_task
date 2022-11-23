from selenium import webdriver
from pages.main_page import *
from pages.shoes_page import *
import pytest
def test_purchase_one_shoes():
    driver = webdriver.Chrome(executable_path='/resource/chromedriver.exe')

    mp = Main_page(driver)
    mp.move_to_shoes_section()

    sp = Shoes_page(driver)
    sp.setting_filtres()
    sp.move_to_item_hoka()

