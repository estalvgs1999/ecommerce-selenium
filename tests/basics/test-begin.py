import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class TestModule(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)


    def test_connect_to_web(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    
    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')


    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

    
if __name__ == '__main__':
    unittest.main(verbosity=2, 
        testRunner=HTMLTestRunner(output='reports', report_name='test module'))