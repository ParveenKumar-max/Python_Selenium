import time

from playwright.sync_api import Playwright, expect


# The URL we passed is here is for another ID.
#-> api call from the browser-> api call contact server return back response to browser-> browser use response to generate html

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69abd66c415d779f9b5f4e3e")

# In below test script, we logged in with different user and pass, route the request with different order ID.
 # Now while Intercepting the network, we have one function "route", and we use * --> accept all request

def test_NetworkIntercepting(playwright:Playwright):
    #page.goto("https://rahulshettyacademy.com/client")
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    print(page.title())

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    # Enter the login credentials 8882698735
    page.get_by_placeholder("email@example.com").fill("pintudogra@gmail.com")
    page.locator("#userPassword").fill("Pintudogra@123")
    page.get_by_role("button").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)