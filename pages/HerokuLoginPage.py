from selenium.webdriver.common.by import By

class HerokuLogin:

    URL = 'https://the-internet.herokuapp.com/login'

    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON = (By.CSS_SELECTOR, "button.radius")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def submit_credentials(self, username, password):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.BUTTON).click()
