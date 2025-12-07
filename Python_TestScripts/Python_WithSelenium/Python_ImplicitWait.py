# Working on Implicit wait

import time
from subprocess import check_output

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

#Edge Driver services 141 -> 141 edge driver
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")  #You can use when we will work on VPN.
driver = webdriver.Edge(service=service_object)
driver.implicitly_wait(5) # If you add implicit, it wil check all program, but not for elements ( where we get list)

#driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("CA")
driver.find_element(By.CSS_SELECTOR,"button[class='search-button']").click()

time.sleep(5)

Fruits_Selected = driver.find_elements(By.XPATH, "//div[@class='products']/div")
Count = len(Fruits_Selected)
print(Count)
assert Count > 0
# EXPLICIT WAIT – wait for each Add to Cart button to be clickable
for result in Fruits_Selected:
    result.find_element(By.CSS_SELECTOR, "div[class='product-action']").click()

print("Add To Cart Selected")

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()


driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,"button[class='promoBtn']").click()

Expected = driver.find_element(By.XPATH,"//span[text()='Code applied ..!']").text
Actual = "Code applied ..!"
assert Actual == Expected

print("Code Applied Successfully")






