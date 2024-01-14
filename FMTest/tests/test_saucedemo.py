
from pages.login_page import LoginPage
from pages.archive_page import ArhivaPage
import time

def test_fit_webpage(driver):
    login_page = LoginPage(driver)
    arhiva_page = ArhivaPage(driver)

    login_page.go_to()

    login_page.login("IB200087", "fafarona951")

    assert login_page.is_at_home_page()

    arhiva_page.click_on_arhiva_link()

    driver.quit()
