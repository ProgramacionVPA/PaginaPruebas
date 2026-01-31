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

    
    def test_busqueda_por_clase(self):
        """Busca el <h1> por CLASS_NAME y valida parte del texto."""
        self.driver.get("https://programacionvpa.github.io/PaginaPruebas/")
        elemento = self.driver.find_element(By.CLASS_NAME, "titulo-principal")
        self.assertIn("Bienvenido", elemento.text)

    def test_busqueda_por_link_text(self):
        """Busca el link exacto por su texto visible."""
        self.driver.get("https://programacionvpa.github.io/PaginaPruebas/")
        link = self.driver.find_element(By.LINK_TEXT, "Ir a Google")
        self.assertEqual(link.get_attribute("id"), "link-google")

    def test_busqueda_por_partial_link_text(self):
        """Busca un link por coincidencia parcial en su texto."""
        self.driver.get("https://programacionvpa.github.io/PaginaPruebas/")
        link_parcial = self.driver.find_element(By.PARTIAL_LINK_TEXT, "ejemplo")
        self.assertEqual(link_parcial.get_attribute("class"), "link-ejemplo")
        

if __name__ == "__main__":
    unittest.main(verbosity=2)

    