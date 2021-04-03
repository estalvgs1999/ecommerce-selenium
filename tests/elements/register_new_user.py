import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    
    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a').click()
        driver.find_element_by_link_text('Log In').click()
        
        create_account_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_btn.is_displayed() and create_account_btn.is_enabled())
        create_account_btn.click()

        self.assertEqual('Create New Customer Account',driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        newsletter_subscription = driver.find_element_by_id('is_subscribed')
        submit_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        # We can code an assert to validate is the fields are enabled

        first_name.send_keys('Alex')
        middle_name.send_keys('Forex')
        last_name.send_keys('Gates') 
        email_address.send_keys('alex@mail.com')
        password.send_keys('5ecure_Passw0rd')
        confirm_password.send_keys('5ecure_Passw0rd')
        newsletter_subscription.click()
        driver.implicitly_wait(10)
        submit_btn.click()
        

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)