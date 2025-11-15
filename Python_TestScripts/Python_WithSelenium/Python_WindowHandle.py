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

#Store Parent window Handle
Parent_window = driver.current_window_handle

Title = driver.find_element(By.XPATH,"//h1[text()='Practice Page']").text
print(Title)
driver.find_element(By.ID,"openwindow").click()

Window = driver.window_handles

# Switch to Window Handles
driver.switch_to.window(Window[1])

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located
           ((By.XPATH,"//a[text()='Access all our Courses']")))

Child_window = driver.find_element(By.XPATH, "//a[text()='Access all our Courses']").text
print(Child_window)

driver.close()
driver.switch_to.window(Window[0])

assert "Practice Page" == Title
print("Child Window closed and driver moved to Parent window.")


