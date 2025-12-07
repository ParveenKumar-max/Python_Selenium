import time
from unittest import expectedFailure

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


Folder_path = "C:/Users/Default/Documents/msedgedriver.exe"
service = Service(Folder_path)
driver = webdriver.Edge(service=service)

#ADDING WAIT CLASS
wait = WebDriverWait(driver, 10)

#OPEN THE URL
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
URL = driver.current_url
driver.maximize_window()
print(URL)

#DOWNLOADED FILE
wait.until(expected_conditions.visibility_of_element_located((By.ID,"downloadButton")))
Downloaded_file = driver.find_element(By.ID,"downloadButton")
Downloaded_file.click()
print("File Downloaded Successfully")

#UPLOADED FILE
File_path = "C:/Users/Parveen/PythonProject_Scratch/FileUpload_Testing.xlsx"
File_upload = driver.find_element(By.XPATH, "//input[@type='file']")
File_upload.send_keys(File_path)
print("File Uploaded Successfully")

#UPLOADED FILE MESSAGE
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")))
Upload_message = driver.find_element(By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
UploadMsgDisplay = Upload_message.text
print(f"Upload Data File:",{UploadMsgDisplay})
time.sleep(5)

#CHECK ELEMENTS
Expected_value  = "Mango"
Fruit_name = driver.find_element(By.XPATH,"//div[@id='row-0']//div[@id='cell-2-undefined']")
Fruits_value = Fruit_name.text
print(Fruits_value)
assert Fruits_value == Expected_value

#STORE ELEMENT IN LIST

List_items_Value = []

All_Fruits = driver.find_elements(By.XPATH,"//div[@class='sc-hIPBNq eXWrwD rdt_TableBody']")
for All_items in All_Fruits:
    Dict_Values = All_items.text.split("\n")
    List_items_Value.append(Dict_Values)

print(List_items_Value)