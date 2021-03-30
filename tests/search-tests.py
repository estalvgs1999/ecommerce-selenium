import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path = r'driver/chromedriver')
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(1)


    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')


    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    
    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    
    def test_search_btn_enabled(self):
        btn = self.driver.find_element_by_class_name('button')


    def test_count_of_promo_banner_imgs(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))


    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_elements_by_css_selector('div.header-minicart span.icon')

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)