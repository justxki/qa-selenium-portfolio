from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BingResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, '.b_algo h2 a')
    SEARCH_INPUT = (By.ID, 'sb_form_q')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )
        return element.get_attribute('value')

    def title(self):
        return self.browser.title