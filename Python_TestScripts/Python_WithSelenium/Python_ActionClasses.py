# Working on Action CLasses wait

import time
from subprocess import check_output


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Edge Driver services
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")
driver = webdriver.Edge(service=service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action  = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()

# How to Right click on Button or any other text

action.context_click(driver.find_element(By.ID,"mousehover")).perform()

driver.implicitly_wait(5)

print("MouseHover Selected")

action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Top']")).perform()
action.move_to_element(driver.find_element(By.XPATH,"//a[text()='Reload']")).click()

time.sleep(3)

