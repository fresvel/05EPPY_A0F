import unittest
from selenium import webdriver

class BrowserDriver (unittest.TestCase):

    _driver_path=None
    @classmethod
    def setUpClass(cls):
        options=webdriver.ChromeOptions()
        options.binary_location=cls._driver_path
        cls._driver_=webdriver.Chrome(options)
        cls._driver_.get("http://localhost:8000")
        

    @classmethod
    def tearDownClass(cls):
        cls._driver_.quit()