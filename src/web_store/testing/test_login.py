import time
from .browser_driver import BrowserDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from flask import session

class TestLogin(BrowserDriver):
    
    def test_get_login_page(self):
        self.assertIn("Login", self._driver_.title)  

    def test_successful_login(self):
        user_input = self._driver_.find_element(By.NAME, "username")
        pass_input =self._driver_.find_element(By.NAME, "password")
        user_input.send_keys("testuser")
        pass_input.send_keys("testpass")
        time.sleep(1)  
        user_input.send_keys(Keys.RETURN)
        time.sleep(1)  
        self.assertIn("home", self._driver_.current_url)

    



