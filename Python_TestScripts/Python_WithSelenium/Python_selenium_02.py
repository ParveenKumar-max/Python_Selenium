# Selenium Script open page and print the title
import time

from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/practice-project")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(3)