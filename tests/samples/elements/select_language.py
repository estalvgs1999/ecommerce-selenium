import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')


    def test_select_language(self):
        driver = self.driver
        exp_options = ['English','French','German']
        act_options = []

        select_language = Select(driver.find_element_by_id('select-language'))
        self.assertEqual(3, len(select_language.options))

        for opt in select_language.options:
            act_options.append(opt.text)

        self.assertListEqual(exp_options,act_options)

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')
        self.assertTrue('store=german', driver.current_url)

        select_language = Select(driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)


    
    def tearDown(self) -> None:
        self.driver.quit()

    
if __name__ == '__main__':
    unittest.main(verbosity=2)