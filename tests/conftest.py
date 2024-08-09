import pytest
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption("--search", action="store", default=None, help="content to search")


@pytest.fixture(scope="class")
def launch_google(pytestconfig):
    search=pytestconfig.getoption("search")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        yield page, search
        browser.close()