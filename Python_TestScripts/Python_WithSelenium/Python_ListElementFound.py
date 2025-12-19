# Select Dynamic Dropdown via Python in Selenium

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

#Edge Driver services 141 -> 141 edge driver
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")  #You can use when we will work on VPN.
driver = webdriver.Edge(service=service_object)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("ind")
driver.implicitly_wait(5)
List_items = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
print(List_items.__getattribute__)
print(len(List_items))
for Select_list in List_items:
    if Select_list.text == "India":
        Select_list.click()
        break

assert driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("India") == "India"

time.sleep(5)