from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()  # Or use webdriver.Firefox()

# Open a website
driver.get("https://www.example.com")

# Verify the title
assert "Example Domain" in driver.title

# Close the browser
driver.quit()
