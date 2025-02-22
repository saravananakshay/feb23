import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    """Setup and teardown for Selenium WebDriver"""
    
    driver = webdriver.Chrome()  # Change to Firefox() or Edge() if needed
    driver.implicitly_wait(5)
    
    yield driver  

    driver.quit()
