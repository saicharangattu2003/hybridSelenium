import pytest
import time
import unittest
from selenium import webdriver
from pages.jiomart_page import JioMartPage
class Test_Execution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        url = "https://www.jiomart.com/"
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()

    def test_JioMart(self):
        time.sleep(2)
        jioObj = JioMartPage(self.driver)
        jioObj.JioMartPageMethods()