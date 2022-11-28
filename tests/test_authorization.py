from selenium import webdriver
from pages.main_page import *
from pages.login_page import *

import allure

from selenium.webdriver.chrome.options import Options

def test_success_authorization():
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/resource/chromedriver.exe', chrome_options=option)

    mp = Main_page(driver)
    mp.move_to_login_section()

    lp = Login_page(driver)
    lp.auth()

    mp.check_authorization()
