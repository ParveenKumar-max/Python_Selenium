import json
import os
import pytest
from playwright.sync_api import Playwright

from E2E_PlaywrightPython_Framework.PageObject.login import loginpage
from E2E_PlaywrightPython_Framework.Utils.Base_WebAPI_PlaywrightPython import APIUtils

file_path = os.path.join(os.path.dirname(__file__), "../data/dataFile.json")

with open(file_path) as file:
    text_data = json.load(file)

user_credentials_list = text_data['User_Credentials_data']


@pytest.mark.parametrize('User_Credentials_data', user_credentials_list)
def test_E2EWebAPI_Validation(playwright: Playwright, User_Credentials_data, openbrowser):
    userName = User_Credentials_data["userEmail"]
    password = User_Credentials_data["userPassword"]

    # Create Order via API
    apiutils = APIUtils()
    OrderID = apiutils.test_OrderCreator(playwright, User_Credentials_data)
    assert OrderID is not None, "Order creation failed — OrderID is None"

    # Login
    login_page = loginpage(openbrowser)
    login_page.loginNavigate()

    # Chain through pages
    dashboard_page = login_page.enter_details(userName, password)
    order_history = dashboard_page.selectOrderNavigation()
    order_detail = order_history.selectOrder(OrderID)
    order_detail.orderDetail()