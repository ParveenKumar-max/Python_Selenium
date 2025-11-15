# Working on Sum Functionalities wait

import time
from subprocess import check_output


from selenium import webdriver
from selenium.webdriver.common.by import By
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

# EXPLICIT WAIT – wait until product list loads
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='products']/div")))

Fruits_Selected = driver.find_elements(By.XPATH, "//div[@class='products']/div")
Count = len(Fruits_Selected)
print(Count)
assert Count > 0
# EXPLICIT WAIT – wait for each Add to Cart button to be clickable
for result in Fruits_Selected:
    wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div[class='product-action']")))
    result.find_element(By.CSS_SELECTOR, "div[class='product-action']").click()

print("Add To Cart Selected")

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

# Wait for checkout button
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")))
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//tr/td[5]/p")))

#checking the prices is matching with expected one or not
prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
count = len(prices)
print(count)
AddFirst = 0
for result in prices:
    AddFirst = AddFirst + int(result.text)
    print(AddFirst)

# Promo code wait
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "input[class='promoCode']")))
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()

# Wait for success message
wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class='promoInfo']"), "Code applied ..!"))

Expected = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
Actual = "Code applied ..!"
assert Actual == Expected
print("Code Applied Successfully")


# Get total amount in variable, Because values are coming in floats, and webdriver can't match or compare text

Total_amount = float(driver.find_element(By.CSS_SELECTOR,"span[class='totAmt']").text)
Total_discount_amount = float(driver.find_element(By.CSS_SELECTOR,"span[class='discountAmt']").text)

if Total_discount_amount < Total_amount:
    print(f"Total Discounted Amount Applied",{Total_discount_amount})
else:
    print(f"Total Discounted Amount Applied Not Applied", {Total_discount_amount})

assert Total_discount_amount < Total_amount
print("Total_discount_amount is lesser then Total_amount", {Total_discount_amount}, {Total_amount})
