import pytest


@pytest.mark.parametrize("item", [
    "MacBook Pro",
    "Mac Mini",
    "Linux Notebook"
])
@pytest.mark.regressiontest
def test_amazon_search_title_multiple(browser,item):
    browser.get("https://www.amazon.com/")
    browser.find_element_by_id("twotabsearchtextbox").send_keys(item)
    browser.find_element_by_id("nav-search-submit-button").click()
