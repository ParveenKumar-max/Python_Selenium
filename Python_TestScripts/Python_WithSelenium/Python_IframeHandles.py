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

wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.ID, "courses-iframe")))

driver.switch_to.frame(driver.find_element(By.ID, "courses-iframe"))


Iframe_text = driver.find_element(By.XPATH,"//div[text()='Trusted by 1 Million+ Students']")
driver.execute_script("arguments[0].scrollIntoView();", Iframe_text)
print(Iframe_text.text)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[text()='JOIN NOW']")))
driver.find_element(By.XPATH,"//a[text()='JOIN NOW']").click()

driver.switch_to.default_content()
Window = driver.window_handles
driver.switch_to.window(Window[1])

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//h3[text()='Sign Up']")))
Sign_up = driver.find_element(By.XPATH,"//h3[text()='Sign Up']").text
print(Sign_up)
driver.close()

driver.switch_to.window(Window[0])

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//h1[text()='Practice Page']")))
Practice_page = driver.find_element(By.XPATH,"//h1[text()='Practice Page']")
driver.execute_script("arguments[0].scrollIntoView();", Practice_page)
print(Practice_page.text)

time.sleep(3)