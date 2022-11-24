import datetime
import time

class Base():
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('the word is correct')
    def get_screenshot(self):
        time.sleep(1)
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H-%M-%S")
        name_screenshot = "screenshot_" + str(now_date) + '.png'
        self.driver.save_screenshot('C:\\Users\\luchk\\GitHub\\RunLab_test_task\\screen' + name_screenshot)
