from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import pytest
from pages.main_page import MainPage



class TestGoogle:
    
    def test_launch(self, launch_google):
        
        page, search=launch_google
        main_page = MainPage(page)
        #launch_google.screenshot(path='screenshot.png')
        assert main_page.search(search)