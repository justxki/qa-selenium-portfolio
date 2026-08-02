from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HerokuDynamicLoad:

    URL = 'https://the-internet.herokuapp.com/dynamic_loading/1'

    LOADED_TEXT = (By.CSS_SELECTOR, "h4:nth-child(1)")
    START_BUTTON = (By.CSS_SELECTOR, "button")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def hit_button(self):
        self.browser.find_element(*self.START_BUTTON).click()

    def loaded_text(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.LOADED_TEXT)
        )
        return element