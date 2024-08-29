import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        service =service(executable_path="C:\dchrome\chromedriver")
        self.driver = webdriver.Chrome(service=service)

    def test_buscar(self):
        driver = self.driver
        driver.get("https://google.com")
        self.assertIn("google", driver.title)
        elemento=driver.find_element("name","q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento" not in driver.page_source
    
    def tearDown(self) -> None:
        Self.driver.close()
if __name__ == "__main__":
    unittest.main()




