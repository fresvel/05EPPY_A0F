import time
from .browser_driver import BrowserDriver
from selenium.webdriver.common.by import By

class TestAuth(BrowserDriver):

    def setUp(self):
        self._driver_.delete_all_cookies()

    def test_home_authentication(self):
            self._driver_.get("http://localhost:8000/home")
            username_field = self._driver_.find_element(By.NAME, "username")
            self.assertIsNotNone(username_field)

    def test_store_authentication(self):
        self._driver_.delete_all_cookies()
        self._driver_.get("http://localhost:8000/store")
        username_field=self._driver_.find_element(By.ID, "username")
        time.sleep(3)
        self.assertIsNotNone(username_field)