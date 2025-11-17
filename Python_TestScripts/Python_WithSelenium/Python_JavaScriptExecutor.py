#Working on JavaScript Executor
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

Edge_options = webdriver.EdgeOptions()
#Edge_options.add_argument("headless")
Edge_options.add_argument("incognito")
Edge_options.add_argument("start-maximized")
Edge_options.add_argument("ignore-certificate-errors")  # remove ssl issue from site

Service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")
driver = webdriver.Edge(service=Service_object, options=Edge_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,1000);")
print("Page Scroll to Iframe")
time.sleep(5)


