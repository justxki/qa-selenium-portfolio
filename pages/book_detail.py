from selenium.webdriver.common.by import By

class BookDetailPage:

    BOOK_TITLE_MAIN = (By.CSS_SELECTOR, '#content_inner h1')
    BOOK_PRICE_MAIN = (By.CSS_SELECTOR, '.product_main .price_color')
    BOOK_STOCK_MAIN = (By.CSS_SELECTOR, '.product_main .instock')

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.find_element(*self.BOOK_TITLE_MAIN).text

    def price(self):
        return self.browser.find_element(*self.BOOK_PRICE_MAIN).text

    def stock(self):
        return self.browser.find_element(*self.BOOK_STOCK_MAIN).text