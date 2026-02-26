import time

from playwright.sync_api import Playwright, expect

from PlaywrightPython_Scratch.utils.Base_Web_APi_Flow import APIUtils


# Automate the Web API

def test_E2EWebAPI_Validation(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False) # By Default, headless is true
    context = browser.new_context()
    page = context.new_page()

    #create Order Id
    apiutils = APIUtils()
    OrderID = apiutils.test_OrderCreater(playwright)

    page.goto("https://rahulshettyacademy.com/client")

    # Enter the login credentials 8882698735
    page.get_by_placeholder("email@example.com").fill("parveendogra2@gmail.com")
    page.locator("#userPassword").fill("Qwerty12345@")
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
