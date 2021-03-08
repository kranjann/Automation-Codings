import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element_by_xpath("//input[@id='autosuggest']").send_keys("ind")
time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
#print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"
