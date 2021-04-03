# Typos

import unittest
from selenium import webdriver

class TyposTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/typos')
        driver.maximize_window()


    def test_typos(self):
        driver = self.driver

        attempts = 0
        detected = False
        
        while not detected:
            attempts += 1
            text_field = driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]').text
            detected = 'won,t' in text_field
            driver.refresh()

        print(f'[Total attempts] : {attempts}')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)