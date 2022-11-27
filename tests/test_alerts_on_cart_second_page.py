from selenium import webdriver
from pages.main_page import *
from pages.shoes_page import *
from pages.product_page import *
from pages.cart_first_page import *
from pages.cart_second_page import *
from pages.order_info_page import *

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def test_alerts_on_cart_second_page():
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    #option.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(executable_path='/resource/chromedriver.exe', chrome_options=option)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    mp = Main_page(driver)
    mp.move_to_shoes_section()

    sp = Shoes_page(driver)
    sp.setting_filtres()
    sp.open_item_product()

    pp = Product_page(driver)
    pp.add_shoes_to_cart()

    cfp = Cart_page_1(driver)
    cfp.move_to_second_step_order()

    csp = Cart_page_2(driver)
    csp.request_alert_on_second_cart_page()

