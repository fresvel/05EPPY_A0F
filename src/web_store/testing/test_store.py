import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .browser_driver import BrowserDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestStore(BrowserDriver):


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
    
    def test_get_store_page(self):
        self._driver_.get("http://localhost:8000/store")
        self.assertIn("store", self._driver_.current_url)
        

    def test_add_item(self):
        print("Adding element")
        self._driver_.get("http://localhost:8000/store")

        # Interactuar con el campo 'q_speaker' y hacer clic en el botón 'b_speaker'
        cantidad_input = self._driver_.find_element(By.ID, "q_speaker")
        cantidad_input.send_keys("1")
        send_button = self._driver_.find_element(By.ID, "b_speaker")
        self._driver_.execute_script("arguments[0].click();", send_button)

        # Interactuar con el campo 'q_laptop' y hacer clic en el botón 'b_laptop'
        cantidad_input = self._driver_.find_element(By.ID, "q_laptop")
        cantidad_input.send_keys("2")
        send_button = self._driver_.find_element(By.ID, "b_laptop")
        self._driver_.execute_script("arguments[0].click();", send_button)

        # Interactuar con el campo 'q_mouse' y hacer clic en el botón 'b_mouse'
        cantidad_input = self._driver_.find_element(By.ID, "q_mouse")
        cantidad_input.send_keys("3")
        send_button = self._driver_.find_element(By.ID, "b_mouse")
        self._driver_.execute_script("arguments[0].click();", send_button)

        # Esperar un poco antes de continuar con el siguiente clic

        # Interactuar con el campo 'q_tv' y hacer clic en el botón 'b_tv'
        cantidad_input = self._driver_.find_element(By.ID, "q_tv")
        cantidad_input.send_keys("4")
        send_button = self._driver_.find_element(By.ID, "b_tv")
        self._driver_.execute_script("arguments[0].click();", send_button)

        # Interactuar con el campo 'q_headset' y hacer clic en el botón 'b_headset'
        cantidad_input = self._driver_.find_element(By.ID, "q_headset")
        cantidad_input.send_keys("5")
        send_button = self._driver_.find_element(By.ID, "b_headset")
        self._driver_.execute_script("arguments[0].click();", send_button)

        element = self._driver_.find_element(By.ID, "cartData")
        time.sleep(2)
        res = element.get_attribute("textContent").strip()
        self.assertEqual('{"altavoz":11,"headset":51,"laptop":21,"mouse":31,"televisor":41}', res)

    def test_basket_function(self):
        basket_button=self._driver_.find_element(By.ID, "nav_basket")
        self._driver_.execute_script("arguments[0].click();", basket_button)
        label_total=WebDriverWait(self._driver_, 10).until(
            EC.visibility_of_element_located((By.ID, "label_total"))
            )
        self.assertEqual(label_total.text, "Total: 67505")




