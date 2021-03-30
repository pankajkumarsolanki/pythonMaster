from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\264956\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("test")
driver.find_element_by_css_selector("input[name='email']").send_keys("test@test.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("password")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()

d = driver.find_element_by_css_selector("div[class*='alert-success']").text
print(d)

driver.quit()
