# Dynamic Controls

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class DynamicControlsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()


    def test_remove_add(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[1]/button')
        add_btn = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div[1]/form[1]/button'))
        )
        sleep(2)
        add_btn.click()
        sleep(3)
    

    def test_enable_disable(self):
        driver = self.driver
        
        btn_css_selector = '#input-example > button:nth-child(2)'
        enable_btn = driver.find_element_by_css_selector(btn_css_selector)
        enable_btn.click()

        disable_btn = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR,btn_css_selector))
        )

        text_input = driver.find_element_by_css_selector('#input-example > input:nth-child(1)')
        text_input.send_keys('Platzi')
        sleep(2)

        disable_btn.click()
        WebDriverWait(driver,20).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR,btn_css_selector))
        )
        sleep(2)


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2) 