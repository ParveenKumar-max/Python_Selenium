import time

from playwright.sync_api import Page

# The URL we passed is here is for another ID.
#-> api call from the browser-> api call contact server return back response to browser-> browser use response to generate html

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69ab1e28415d779f9b5e4b7c")

# In below test script, we logged in with different user and pass, route the request with different order ID.

def test_NetworkIntercepting(page:Page):
    page.goto("https://rahulshettyacademy.com/client")

    # Now while Intercepting the network, we have one function "route", and we use * --> accept all request

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    # Enter the login credentials 8882698735
    page.get_by_placeholder("email@example.com").fill("parveendogra2@gmail.com")
    page.locator("#userPassword").fill("Qwerty12345@")
    page.get_by_role("button").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(5)