# pages/arhiva_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ArhivaPage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_arhiva_link(self):
        xpath_hyperlink = '//*[@id="HyperLink7"]'
        hyperlink_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_hyperlink))
        )
        hyperlink_element.click()

    def select_subject_in_combobox(self, subject_name):
        xpath_combobox = '//*[@id="listPredmet"]'
        combobox_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_combobox))
        )

        select = Select(combobox_element)
        select.select_by_visible_text(subject_name)

    def enter_text_in_input(self, text):
        xpath_input = '//*[@id="txtRijeci"]'
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_input))
        )
        input_element.clear()
        input_element.send_keys(text)

    def select_option_in_second_combobox(self, option_name):
        xpath_combobox = '//*[@id="listOperator"]'
        combobox_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_combobox))
        )

        select = Select(combobox_element)
        select.select_by_visible_text(option_name)

    def enter_date_in_input(self, date, xpath_input):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_input))
        )
        input_element.clear()
        input_element.send_keys(date)

    def click_search_button(self):
        xpath_button = '//*[@id="btnTrazi"]'
        button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_button))
        )
        button_element.click()

    def get_available_options_in_second_combobox(self):
        xpath_combobox = '//*[@id="listOperator"]'
        combobox_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_combobox))
        )

        select = Select(combobox_element)
        options = [option.text for option in select.options]
        return options