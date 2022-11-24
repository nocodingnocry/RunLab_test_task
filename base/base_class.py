import datetime
import time

class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
       get_url = self.driver.current_url
       print('Current_url: '+ get_url)

    def assert_word(self, word, result):
        assert word == result
        print('the word is correct')

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('URL is correct')
    def get_screenshot(self):
        time.sleep(1)
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H-%M-%S")
        name_screenshot = "screenshot_" + str(now_date) + '.png'
        self.driver.save_screenshot('C:\\Users\\luchk\\GitHub\\RunLab_test_task\\screen' + name_screenshot)
