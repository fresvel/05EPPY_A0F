import unittest
from selenium import webdriver
#from web_store import __main__ as app_main

class BrowserDriver (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #app_main()
        options=webdriver.ChromeOptions()
        #options.binary_location="/home/fresvel/Documentos/Capacitación/Python/Viu/Librerías_y_Proyectos/Actividades/05EPPY_A01/src/chrome-linux/chrome"
        options.binary_location=input("Ingrese la ruta absoluta del driver")
        cls._driver_=webdriver.Chrome(options)
        cls._driver_.get("http://localhost:8000")
        

    @classmethod
    def tearDownClass(cls):
        cls._driver_.quit()