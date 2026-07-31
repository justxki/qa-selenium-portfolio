from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BingSearchPage:

    URL = 'https://www.bing.com/search?q='

    SEARCH_INPUT = (By.CSS_SELECTOR, 'textarea.sb_form_q')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        import time
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        time.sleep(3)
        search_input.send_keys(Keys.RETURN)