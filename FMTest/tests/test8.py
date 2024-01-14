import sys
print(sys.path)

from pages.login_page import LoginPage
from pages.archive_page import ArhivaPage
import time

def test_fit_webpage(driver):
    login_page = LoginPage(driver)
    arhiva_page = ArhivaPage(driver)

    login_page.go_to()
    time.sleep(2)

    login_page.login("IB200087", "fafarona951")
    time.sleep(2)

    assert login_page.is_at_home_page()
    time.sleep(2)

    arhiva_page.click_on_arhiva_link()
    time.sleep(2)

    arhiva_page.select_subject_in_combobox("Matematika I")
    time.sleep(2)

    arhiva_page.select_option_in_second_combobox("Sve riječi (AND)")
    time.sleep(2)

    arhiva_page.click_search_button()
    time.sleep(3)

    driver.quit()
