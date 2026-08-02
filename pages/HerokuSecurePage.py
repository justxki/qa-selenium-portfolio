from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HerokuSecure:

    LOGIN_BANNER = (By.CSS_SELECTOR, "div.flash")

    def __init__(self, browser):
        self.browser = browser

    def banner(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.LOGIN_BANNER)
        )
        return element.text