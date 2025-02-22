from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()  # Or use webdriver.Firefox()

# Open a website
driver.get("https://www.wikipedia.com")

# Verify the title
assert "wikipedia" in driver.title

# Close the browser
driver.quit()
