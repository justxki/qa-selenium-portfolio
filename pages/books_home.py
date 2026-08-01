from selenium.webdriver.common.by import By

class BooksHomePage:

    URL = 'https://books.toscrape.com/catalogue/page-3.html'

    SELECT_BOOK_TITLE = (By.CSS_SELECTOR, 'h3 a')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def click_book(self):
        self.browser.find_elements(*self.SELECT_BOOK_TITLE)[1].click()