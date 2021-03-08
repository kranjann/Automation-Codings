from selenium import webdriver

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.google.com/help")
driver.back()
driver.refresh()
driver.close()