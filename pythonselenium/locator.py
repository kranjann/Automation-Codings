from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "/usr/local/bin/chromedriver")
driver.get("https://www.google.com")
driver.maximize_window()

#using name attribute
#driver.find_element_by_name("q").send_keys("krishna")

#using CSS Slector
#driver.find_element_by_css_selector("input[name='q']").send_keys("Krishna")

#using css selector for ID
#driver.find_element_by_css_selector("")

#using xpath selector
driver.find_element_by_xpath("//input[@name='q']").send_keys("Krishna")

#using linktest locator
driver.find_element_by_link_text("About").click()

#issue with following code check later
#driver.find_element_by_xpath("//input[@name='btnK']").click()
#driver.implicitly_wait(2)
#driver.close()
