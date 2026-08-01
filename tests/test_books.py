"""
Book Page Searchin
"""

from pages.books_home import BooksHomePage
from pages.book_detail import BookDetailPage


def test_book_search(browser):
    book_home = BooksHomePage(browser)
    book_detail = BookDetailPage(browser)

    #Given
    book_home.load()

    #When ##Pycharm lowkey gave me the answer lol bishhh
    book_home.click_book()

    #Then
    assert "£" in book_detail.price()
    assert "In stock" in book_detail.stock()
    assert book_detail.title()  # non-empty string is truthy
    ## or assert book_detail.title() != ""      # explicit empty check
    ## or assert len(book_detail.title()) > 0   # explicit length check