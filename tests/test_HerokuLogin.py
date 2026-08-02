from pages.HerokuLoginPage import HerokuLogin
from pages.HerokuSecurePage import HerokuSecure

def test_LoginSubmit(browser):
    login_page = HerokuLogin(browser)
    secure_page = HerokuSecure(browser)

    login_page.load()

    login_page.submit_credentials("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in secure_page.banner()

