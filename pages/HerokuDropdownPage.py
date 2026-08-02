from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HerokuDropdown:

    URL = 'https://the-internet.herokuapp.com/dropdown'

    DROPDOWN = (By.CSS_SELECTOR, "select")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def choose_option(self, option_text):
        dropdown = Select(self.browser.find_element(*self.DROPDOWN))
        dropdown.select_by_visible_text(option_text)

    def selected_option(self):
        dropdown = Select(self.browser.find_element(*self.DROPDOWN))
        return dropdown.first_selected_option.text