# Working on different Locators with different Types
# Select Dynamic Dropdown, Radio Button, Checkbox, Alert, Element Displayed via Python in Selenium

import time
from subprocess import check_output

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

#Edge Driver services 141 -> 141 edge driver
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")  #You can use when we will work on VPN.
driver = webdriver.Edge(service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Select Radio Button
Radio_button = driver.find_element(By.XPATH,"//div[@id='radio-btn-example']")
driver.find_element(By.XPATH,"//input[@value='radio1']").click()

#Input Type
Input_Type = driver.find_element(By.XPATH, "//input[@id='autocomplete']")
Input_Type.send_keys("Automation Scripting")

# Select Dropdown Button
Dropdown_value = Select(driver.find_element(By.ID,"dropdown-class-example"))
Dropdown_value.select_by_value("option3")

#Checkbox
Checkbox_value = driver.find_element(By.ID,"checkbox-example")
Checkbox_selected = driver.find_element(By.XPATH, "//input[@value='option2']")
Checkbox_selected.click()
print("Checking ", Checkbox_selected.is_selected())

#Open Window
Window_Open = driver.find_element(By.ID,"openwindow")
Window_Open.click()
Windows = driver.window_handles
print("Windows Handles !", Windows)
driver.switch_to.window(Windows[1])
print("Switched Window !", driver.title)

driver.switch_to.window(Windows[0])

time.sleep(3)

#Open Tab
Window_tab = driver.find_element(By.ID,"id='opentab")
Window_tab.click()

#Handle Alert
Window_Alert = driver.find_element(By.ID, "name")
Window_Alert.send_keys("Parveen")

Alert = driver.find_element(By.ID, "alertbtn").click
Pop_up = driver.switch_to.alert
Pop_up.accept()



time.sleep(5)
