import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#code to handle Java/JS pop-up alerts
driver.find_element_by_css_selector("#name").send_keys("Krishna")
driver.find_element_by_css_selector("#alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()

#negative case using alert.dismiss()
driver.find_element_by_xpath("//input[@id='name']").send_keys("Ranjan")
driver.find_element_by_xpath("//input[@id='confirmbtn']").click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.dismiss()

