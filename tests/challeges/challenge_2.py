# Disappearing Elements

import unittest
from selenium import webdriver

class AddRemoveElements(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Disappearing Elements').click()


    def test_disappearing_elements(self):
        driver = self.driver

        attempts = 0
        done = False

        while not done:
            attempts += 1
            try:
                driver.find_element_by_link_text('Gallery')
                done = True
            except Exception:
                driver.refresh()

        print(f'[Total attempts] : {attempts}')
        

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2) 