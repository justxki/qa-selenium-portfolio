"""
These tests cover Bing searches.
"""
import pytest
from pages.result_practice import BingResultPage
from pages.search_practice import BingSearchPage

@pytest.mark.parametrize('phrase', ['wolfsbane', 'nightshade', 'belladonna'])
def test_basic_bing_search(browser, phrase):

  search_page = BingSearchPage(browser)
  result_page = BingResultPage(browser)

  # Given the Bing home page is displayed
  search_page.load()

  # When the user searches for "wolfsbane"
  search_page.search(phrase)

  # And the search result query is "wolfsbane"
  assert phrase in result_page.search_input_value()

  # And the search result links pertain to "wolfsbane"
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0

  # TODO: Remove this exception once the test is complete
  #raise Exception("Incomplete Test")