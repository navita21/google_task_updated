import pytest
from playwright.sync_api import Page

class MainPage():
    def __init__(self, page:Page):
        self.page=page
    def search(self, search: str=None):
        
        search_bar=self.page.locator('//*[@id="APjFqb"]')
        if search_bar.is_visible():
            search_bar.fill(search)
            google_search = self.page.get_by_label("Google Search").nth(0)
            google_search.click()
            self.page.wait_for_load_state('networkidle')
            self.page.wait_for_selector('h3')

            # Select the first 10 search results
            results = self.page.locator('h3').all_text_contents()[:10]
            self.page.wait_for_load_state('networkidle')

            # Print the results to the console
            for idx, result in enumerate(results, start=1):
             print(f"{idx}. {result}")

            # Write the results to a text file
            with open("search_results.txt", "w") as file:
                for idx, result in enumerate(results, start=1):
                    file.write(f"{idx}. {result}\n")
                return True
        return False

