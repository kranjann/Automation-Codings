from selenium import webdriver

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkBox = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(checkBox))

for chckbox in checkBox:
    if chckbox.get_attribute('value') == "option2":
      chckbox.click()
      assert chckbox.is_selected()

radiobuttons = driver.find_elements_by_xpath("//input[@name='radioButton']")

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()
        assert radiobutton.is_selected()
