# test_saucedemo.py

from pages.login_page import LoginPage
from pages.archive_page import ArhivaPage
import time

def test_fit_webpage(driver):
    login_page = LoginPage(driver)
    arhiva_page = ArhivaPage(driver)

    # Open the Fit.ba login page
    login_page.go_to()

    # Log in with provided credentials
    login_page.login("IB200087", "fafarona951")

    # Check if the login was successful and the user is on the home page
    assert login_page.is_at_home_page()

    # Navigate to Arhiva page
    arhiva_page.click_on_arhiva_link()

    # Select "Matematika I" from the first combobox
    arhiva_page.select_subject_in_combobox("Matematika I")

    # Enter "rezultati usmenog" in the input field
    arhiva_page.enter_text_in_input("rezultati usmenog")

    # Select "Sve riječi (AND)" from the second combobox
    arhiva_page.select_option_in_second_combobox("Sve riječi (AND)")

    # Enter "01.09.2021" in the date input field
    arhiva_page.enter_date_in_input("01.09.2021", '//*[@id="txtDatumOd"]')

    # Enter "01.09.2022" in the date input field
    arhiva_page.enter_date_in_input("01.09.2022", '//*[@id="txtDatumDo"]')

    # Click the "Traži" button
    arhiva_page.click_search_button()

    # Adding a sleep for visualization purposes (can be removed in real use)
    time.sleep(5)

    # Close the browser window
    driver.quit()
