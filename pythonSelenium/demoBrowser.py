from selenium import webdriver

# every browser exposes an executable file. Hence need to invoke this file through selenium test > inturn invokes actual browser

driver = webdriver.Chrome(executable_path="C:\\Users\\264956\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Users\\264956\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Users\\264956\\IEDriverServer.exe")

driver.get("https://www.google.co.in")
print(driver.title)
print(driver.current_url)
# driver.close() #closes current browser window

driver.get("https://www.udemy.com")
driver.maximize_window()
driver.get("https://www.google.co.in")
driver.minimize_window()
driver.back()
driver.refresh()
driver.quit() #closes all open browser window
