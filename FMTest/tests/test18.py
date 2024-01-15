import sys
import random
import time
from pages.login_page import LoginPage
from pages.archive_page import ArhivaPage

def test_fit_webpage(driver):
    login_page = LoginPage(driver)
    arhiva_page = ArhivaPage(driver)

    login_page.go_to()
    time.sleep(2)

    login_page.login("VAŠ INDEKS", "VAŠA LOZINKA")
    time.sleep(2)

    assert login_page.is_at_home_page()
    time.sleep(2)

    arhiva_page.click_on_arhiva_link()
    time.sleep(2)

    random_choice = random.choice(["Bilo koja riječ (OR)", "Sve riječi (AND)"])
    available_options = arhiva_page.get_available_options_in_second_combobox()
    if random_choice not in available_options:
        raise ValueError(f"Option '{random_choice}' not available in the dropdown.")    
    arhiva_page.select_option_in_second_combobox(random_choice)
    time.sleep(2)

    arhiva_page.enter_date_in_input("01.09.2021", '//*[@id="txtDatumOd"]')
    time.sleep(2)
    
    arhiva_page.click_search_button()
    time.sleep(3)

    driver.quit()

