import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # Different browsers can be chosen. Tests work for each of them
        # Start tests with only one browser active!
        browser = p.chromium.launch(headless = False)
        #browser = p.firefox.launch()
        #browser = p.webkit.launch()
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    with browser as b:
        page = b.new_page()
        yield page
        page.close()


