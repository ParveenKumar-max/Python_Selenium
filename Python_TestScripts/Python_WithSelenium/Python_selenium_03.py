# Selenium Practice Page with Different locator
# Id, name, linktext, partiallinkText, cssSelector, classname, xPath

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

#Edge Driver services 141 -> 141 edge driver
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")  #You can use when we will work on VPN.
driver = webdriver.Edge(service=service_object)

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
time.sleep(3)
print(f"Tile of the page is : ", driver.title)
# In Java, the way writing the find element code is different.
Email = driver.find_element(By.NAME, "email")
Email.send_keys("rahulshettyacademy")

Password = driver.find_element(By.ID, "exampleInputPassword1")
Password.send_keys("learning")

Submit = driver.find_element(By.XPATH, "//input[@type='submit']")
Submit.click()

Alert_message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(Alert_message)
assert "Success!" in Alert_message




time.sleep(5)

