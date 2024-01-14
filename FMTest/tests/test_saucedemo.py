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

    # Close the browser window
    driver.quit()
