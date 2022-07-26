from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from time import sleep

class app_test_case(unittest.TestCase):


    def setUp(self):
        #chromeOptions = webdriver.ChromeOptions()
        chromeOptions = Options()
        driver_path = '/usr/local/bin/chromedriver'
        #driver_path = "/opt/chromedriver"
        #Changed 'chromeOptions' to 'options'
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('--no-sandbox')


        #self.driver = webdriver.Chrome(driver_path, options=chromeOptions)
        self.driver = webdriver.Chrome(driver_path, options=chromeOptions)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        path = 'https://www.facebook.com/'
        self.base_url = path

    def test_i_d_e_script1(self):
        driver = self.driver
        driver.get(self.base_url)

        get_title = driver.title
        print(get_title)


    def tearDown(self):
        sleep(5)
        self.driver.quit()




if __name__ == "__main__":
    unittest.main()
