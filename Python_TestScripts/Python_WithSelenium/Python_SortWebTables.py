import time
from subprocess import check_output


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.page import print_to_pdf
from selenium.webdriver.common.log import Log
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Edge Driver services
service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")
driver = webdriver.Edge(service=service_object)

wait = WebDriverWait(driver, 5)

driver.get("https://projects.hackerearth.com/p1/index.html")
Page_URL = driver.current_url
driver.maximize_window()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='crud-page']//h1")))
Page_url = driver.title
print(Page_url)

#Enter "Hackerearth" in the input field.

Enter_Input = driver.find_element(By.XPATH,"//input[@type='text']")
Enter_Input.send_keys("Hackerearth")

Add_button = driver.find_element(By.XPATH,"//div[@class='crud-page']/button")
Add_button.click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='crud-page']//ul//li")))
Input_added = driver.find_element(By.XPATH,"//div[@class='crud-page']//ul//li")
print(Input_added.text)

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@id='root']/div/nav/ul/li[3]")))
driver.find_element(By.XPATH,"//div[@id='root']/div/nav/ul/li[3]").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='sort-page']/button[2]")))
driver.find_element(By.XPATH,"//div[@class='sort-page']/button[2]").click()


Page_URL1 = Page_URL
print(Page_URL1)
List1 = []
List_items = driver.find_elements(By.XPATH,"//div[@class='content']/div/ul/li")
for items in List_items:
    List1.append(items.text)

print(List1[0], Page_URL1)


driver.find_element(By.XPATH,"//*[@id='root']/div/nav/ul/li[2]").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='content']/div/ul/li")))
List_items = driver.find_elements(By.XPATH,"//div[@class='content']/div/ul/li")
List2 = []
for items2 in List_items:
    List2.append(items2.text)

Input_added1 = driver.find_element(By.XPATH,"//div[@class='search-page']/input")
Input_added1.send_keys("Item 2")
Search_item = driver.find_element(By.XPATH,"//div[@class='content']/div/ul/li[1]")
print(Search_item.text, Page_URL1)

time.sleep(5)
