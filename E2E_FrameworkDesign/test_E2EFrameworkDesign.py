import json

import pytest

from E2E_FrameworkDesign.PageObject.loginPage import loginPage

test_data_file = "C://Users//Parveen//PythonProject_Scratch//E2E_FrameworkDesign//data//test_E2EFrameworkDesign.json"
with open(test_data_file) as f:
   test_data = json.load(f)
   test_list = test_data["data"]

@pytest.mark.parametrize( "test_list_item", test_list)
def test_E2EFrameworkDesign(browserInstance, test_list_item):
   driver = browserInstance
   login_page = loginPage(driver)      # Create an Object of loginPage & ShopPage
   print(login_page.getTitle())
   shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
   shop_page.clickshop()
   shop_page.selectItems_tocart(test_list_item["productName"])
   print(shop_page.getTitle())

   # Create an Object of checkout_confirmation and pass the username and password

   checkout_confirmation = shop_page.checkout()
   checkout_confirmation.checkout()

   checkout_confirmation.delivery_address("ind")
   print(checkout_confirmation.getTitle())

   print(checkout_confirmation.getTitle())
   checkout_confirmation.delivery_address("ind")
   checkout_confirmation.last_validation()

print("Test Executes Successfully")
print("End To End Selenium with Python Flow is completed Successfully")





