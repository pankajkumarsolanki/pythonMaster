import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\264956\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
# driver.implicitly_wait(10)
searchTerm = "oni"
driver.find_element_by_css_selector(".search-keyword").send_keys(searchTerm)
driver.find_element_by_xpath("//button[@class='search-button']").click()

time.sleep(10)

productList = driver.find_elements_by_xpath("//div[@class='product']/h4")
addToCart = driver.find_elements_by_xpath("//div[@class='product-action']/button")

List = []

if len(productList) == 0:
    print("No Matching Products")
    driver.quit()
    exit(1)
else:
    print("\nSEARCHED PRODUCT CONTAINS SEARCH TERM")
    for i in productList:
        a = i.text
        if searchTerm.lower() in a.lower():
            print(a + " : Contains '" + searchTerm + "' - PASS")
        else:
            print("FAIL")
            driver.quit()
            exit(1)
        List.append(a)
    for a in addToCart:
        a.click()
    print("\nSEARCHED PRODUCT LIST IS:")
    print(List)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

cartProductName = driver.find_elements_by_class_name("product-name")

List2 = []
for a in cartProductName:
    List2.append(a.text)
print("\nCART PRODUCT LIST IS:")
print(List2)
assert (List == List2)

rows = len(driver.find_elements_by_xpath("//tbody//tr"))
columns = len(driver.find_elements_by_xpath("//thead//tr//td"))

print("\nCART DETAILS: \nProduct Name | Quantity | Price | Total")
List3 = []
for row in range(1, rows + 1):
    for column in range(2, columns + 1):
        a = driver.find_element_by_xpath("//tbody//tr[" + str(row) + "]//td[" + str(column) + "]").text
        List3.append(a)
    print(*List3, sep=" | ")
    List3.clear()

print("\n--------------------------------------------------------")

cartPrice = driver.find_elements_by_xpath("//tr/td[5]/p")
sumAs = 0
for a in cartPrice:
    sumAs = sumAs + int(a.text)
print("\n{} {}".format("Sum is : ", sumAs))

driver.quit()
