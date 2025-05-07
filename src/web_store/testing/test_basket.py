import time
from .browser_driver import BrowserDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class TestBasket(BrowserDriver):

    def setUp(self):
        self._esperar_=WebDriverWait(self._driver_, 10)
        self._driver_.get("http://localhost:8000/login")
        try:
            user_input = self._driver_.find_element(By.NAME, "username")
            pass_input =self._driver_.find_element(By.NAME, "password")
            user_input.send_keys("testuser")
            pass_input.send_keys("testpass")
            user_input.send_keys(Keys.RETURN)
            time.sleep(1)
        except Exception as e:
            pass
    
    def test_basket_page(self):
        self._driver_.get("http://localhost:8000/basket")
        label_total=WebDriverWait(self._driver_, 10).until(
            EC.visibility_of_element_located((By.ID, "label_total"))
            )
        self.assertEqual(label_total.text, "Total: 0")
        
    




