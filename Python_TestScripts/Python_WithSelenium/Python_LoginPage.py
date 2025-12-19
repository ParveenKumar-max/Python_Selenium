import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

#Edge Driver services 141 -> 141 edge driver
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")  #You can use when we will work on VPN.
driver = webdriver.Edge(service=service_object)

driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.implicitly_wait(5)

print(driver.get_cookies())
print(driver.current_url)
driver.maximize_window()

Forgot_Password = driver.find_element(By.LINK_TEXT, "Forgot password?")
Forgot_Password.click()

User_email = driver.find_element(By.XPATH, "//input[@formcontrolname='userEmail']")
User_email.send_keys("demo@gmail.com")

User_Password = driver.find_element(By.XPATH, "//input[@formcontrolname='userPassword']")
User_Password.send_keys("Hello@1234")

Confirm_Password = driver.find_element(By.XPATH, "//input[@formcontrolname='confirmPassword']")
Confirm_Password.send_keys("Hello@1234")

Save_Button = driver.find_element(By.XPATH, "//button[@type='submit']")
Save_Button.click()

print("Password Changed Successfully")

driver.implicitly_wait(10)
time.sleep(3)



