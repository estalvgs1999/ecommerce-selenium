import unittest, csv
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
    data_file = open(file_name, mode= 'r')
    reader = csv.reader(data_file)
    next(reader,None)
    rows = [row for row in reader]
    return rows


@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= r'driver/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')


    @data(*get_data(r'tests/workflows/test_data.csv'))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        self.assertEqual(len(products),int(expected_count))


    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)