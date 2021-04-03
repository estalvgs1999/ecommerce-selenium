# Add/ Remove Elements

import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()


    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add? : '))
        elements_removed = int(input('How many elements will you remove? : '))
        total_elements = elements_added - elements_removed

        add_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')

        for x in range(elements_added):
            add_btn.click()

        sleep(2)
        
        for x in range(elements_removed):
            try:
                rmv_btn = driver.find_element_by_class_name('added-manually')
                rmv_btn.click()
            except Exception:
                print('[Error]: There is no more elements to delete!')
                break

        sleep(2)

        if total_elements < 0: total_elements = 0 
        
        print(f'[Total Elements] = {total_elements}')
        

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)