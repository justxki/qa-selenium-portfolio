import pytest

from pages.HerokuLoginPage import HerokuLogin
from pages.HerokuSecurePage import HerokuSecure
from pages.HerokuDropdownPage import HerokuDropdown
from pages.HerokuDynamicLoadPage import HerokuDynamicLoad


def test_login_submit(browser):
    login_page = HerokuLogin(browser)
    secure_page = HerokuSecure(browser)

    login_page.load()

    login_page.submit_credentials("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in secure_page.banner()

def test_dropdown(browser):
    dropdown = HerokuDropdown(browser)

    dropdown.load()

    dropdown.choose_option("Option 1")

    assert dropdown.selected_option() == "Option 1"


def test_dynamic_load(browser):
    dynamic_page = HerokuDynamicLoad(browser)
    dynamic_page.load()
    dynamic_page.hit_button()
    loaded_element = dynamic_page.loaded_text()
    assert loaded_element.is_displayed()
    assert "Hello World!" in loaded_element.text
