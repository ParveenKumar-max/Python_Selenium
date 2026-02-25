import time

from playwright.sync_api import Playwright

from PlaywrightPython_Scratch.utils.Base_Web_APi_Flow import APIUtils


# Automate the Web API

def test_E2EWebAPI_Validation(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False) # By Default, headless is true
    context = browser.new_context()
    page = context.new_page()

    #create Order Id
    apiutils = APIUtils()
    apiutils.test_OrderCreater(playwright)

    page.goto("https://rahulshettyacademy.com/client")

    # Enter the login credentials
    page.get_by_placeholder("email@example.com").fill("parveendogra2@gmail.com")
    page.locator("#userPassword").fill("Qwerty12345@")
    page.get_by_role("button").click()
    time.sleep(5)

    #Checking the API -- Order History page --> Order is Present
    # But before that we have to create a API Class.
