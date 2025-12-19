# Selenium With Python
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

#Edge Driver services 141 -> 141 edge driver
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")  #You can use when we will work on VPN.
driver = webdriver.Edge(service=service_object)


#driver = webdriver.Edge()    #Python people creates service for every browser, Edge driver Services
driver.get("https://www.google.com")
time.sleep(3)