from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()  # Or use webdriver.Firefox()

# Open a website
driver.get("https://www.wikipedia.com")

# Verify the title
assert "Wikipedia" in driver.title

# Close the browser
driver.quit()
