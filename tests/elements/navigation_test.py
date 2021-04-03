import unittest
from selenium import webdriver
from selenium.webdriver.common import service

class NavigationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('https://google.com/')


    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('golden state warriors')
        search_field.submit()

        driver.back()
        driver.forward()
        driver.refresh()

    
    def tearDown(self) -> None:
        self.driver.quit()

    
if __name__ == '__main__':
    unittest.main(verbosity=2)