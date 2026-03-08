import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from E2E_PlaywrightPython_Framework.Utils.Base_WebAPI_PlaywrightPython import APIUtils

# Json file --> Utils --> access into test

with open('../data/dataFile.json') as file:
    text_data = json.load(file)
    print(text_data)
    user_credentials_list = text_data['User_Credentials_data']


# Automate the Web API
@pytest.mark.parametrize('User_Credentials_data', user_credentials_list)
def test_E2EWebAPI_Validation(playwright:Playwright, User_Credentials_data):
    browser = playwright.chromium.launch(headless=False) # By Default, headless is true
    context = browser.new_context()
    page = context.new_page()

    #create Order Id
    apiutils = APIUtils()
    OrderID = apiutils.test_OrderCreator(playwright, User_Credentials_data)
    time.sleep(5)
    page.goto("https://rahulshettyacademy.com/client")
  # Enter the login credentials 8882698735

    page.get_by_placeholder("email@example.com").fill(User_Credentials_data["userEmail"])
    page.locator("#userPassword").fill(User_Credentials_data["userPassword"])
    page.get_by_role("button").click()

    # Order History Page
    page.get_by_role("button",name="ORDERS").click()
    row = page.locator("tr").filter(has_text=OrderID)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
    time.sleep(5)

    #Checking the API -- Order History page --> Order is Present
    # But before that we have to create an API Class.
