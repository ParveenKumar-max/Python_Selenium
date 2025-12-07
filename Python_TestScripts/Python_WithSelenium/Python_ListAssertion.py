# Working on Sum List Assertion wait

import time
from subprocess import check_output


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Edge Driver services
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")
driver = webdriver.Edge(service=service_object)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# EXPLICIT WAIT – wait for search bar to be visible
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@class='search-keyword']")))

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("CA")
driver.find_element(By.CSS_SELECTOR, "button[class='search-button']").click()

# Create a list

Expected_list = ['Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg']
print(f"Actual list of Vege's: {Expected_list}")

# EXPLICIT WAIT – wait until product list loads
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h4[class='product-name']")))

Actual_list = driver.find_elements(By.CSS_SELECTOR, "h4[class='product-name']")
Count = len(Actual_list)
print(Count)
Actual_list1 = []
for items in Actual_list:
    Actual_list1.append(items.text)

if Expected_list != Actual_list1:
    print(f"List Not Matched : {Actual_list1}")
else:
    print(f"List Matched Successfully : {Expected_list}")

assert Actual_list1 == Expected_list
print("List Matched successfully")