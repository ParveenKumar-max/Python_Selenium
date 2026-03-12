import json
import time

import pytest
from playwright.sync_api import Playwright

from E2E_PlaywrightPython_Framework.PageObject.dashboard import dashboard
from E2E_PlaywrightPython_Framework.PageObject.login import loginpage
from E2E_PlaywrightPython_Framework.PageObject.orderDetailsSuccess import orderDetailSuccess
from E2E_PlaywrightPython_Framework.PageObject.orderHistory import orderHistory
from E2E_PlaywrightPython_Framework.Utils.Base_WebAPI_PlaywrightPython import APIUtils

# Json file --> Utils --> access into test
file_path = "C:/Users/Parveen/PythonProject_Scratch/E2E_PlaywrightPython_Framework/data/dataFile.json"
with open(file_path) as file:
    text_data = json.load(file)
    print(text_data)
    user_credentials_list = text_data['User_Credentials_data']


# Automate the Web API
@pytest.mark.parametrize('User_Credentials_data', user_credentials_list)
def test_E2EWebAPI_Validation(playwright:Playwright, User_Credentials_data, openbrowser):
    userName = User_Credentials_data["userEmail"]
    password = User_Credentials_data["userPassword"]

    #create Order Id
    apiutils = APIUtils()
    OrderID = apiutils.test_OrderCreator(playwright, User_Credentials_data)

    #login Page
    login_page = loginpage(openbrowser)
    login_page.loginNavigate()
    login_page.enter_details(userName, password)

    #dashboard Page
    dashboard_page = dashboard(openbrowser)
    dashboard_page.selectOrderNavigation()

    #order History
    order_history = orderHistory(openbrowser)
    order_history.selectOrder(OrderID)

    # order Detail
    order_detail = orderDetailSuccess(openbrowser)
    order_detail.orderDetail()

    # More better way

    #page.wait_for_load_state("networkidle")

    #Checking the API -- Order History page --> Order is Present
    # But before that we have to create an API Class.
