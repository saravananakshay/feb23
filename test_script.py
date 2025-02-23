import pytest
from selenium import webdriver

class TestWikipedia:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.wikipedia.org/")

    def test_title(self):
        assert "wikipedia." in self.driver.title.lower()

    def teardown_method(self):
        self.driver.quit()
