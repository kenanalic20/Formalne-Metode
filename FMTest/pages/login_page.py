from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
class LoginPage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=10)
    def go_to(self):
        self.selenium_driver.get("https://www.fit.ba/student/login.aspx")
 
    def login(self, broj_dosijea, lozinka):
        xpath_broj_dosijea = '//*[@id="txtBrojDosijea"]'
        broj_dosijea_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_broj_dosijea))
        )
        broj_dosijea_input.send_keys(broj_dosijea)
 
        xpath_lozinka = '//*[@id="txtLozinka"]'
        lozinka_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_lozinka))
        )
        lozinka_input.send_keys(lozinka)
 
        xpath_prijava_button = '//*[@id="btnPrijava"]'
        prijava_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_prijava_button))
        )
        prijava_button.click()
 
    def is_at_home_page(self):
        xpath_hyperlink = '//*[@id="HyperLink7"]'
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_hyperlink)))
            return True
        except:
            return False