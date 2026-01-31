import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPaginaPruebasBasica(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Crea el driver de Chrome automáticamente
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_cargar_pagina_y_leer_titulo(self):
        url = "https://programacionvpa.github.io/PaginaPruebas/"
        self.driver.get(url)

        h1 = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("Bienvenido a PaginaPruebas", h1.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)