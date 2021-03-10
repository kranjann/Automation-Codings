from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(4)

elements = driver.find_elements_by_xpath("//div[@class='products']/div")
count = len(elements)
assert count == 3

addButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in addButtons:
    button.click()

time.sleep(4)

driver.find_element_by_css_selector("img[alt='Cart']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()

message = driver.find_element_by_class_name("promoInfo").text
assert message == "Code applied ..!"

