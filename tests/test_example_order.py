from selenium import webdriver
from pages.main_page import *
from pages.shoes_page import *
from pages.product_page import *
from pages.cart_first_page import *
from pages.cart_second_page import *
from pages.order_info_page import *

from selenium.webdriver.chrome.options import Options
def test_purchase_one_shoes(set_up):
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/resource/chromedriver.exe', chrome_options=option)

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
    csp.completion_ordering()

    oip = Order_info_class(driver)
    oip.finish_screen()

