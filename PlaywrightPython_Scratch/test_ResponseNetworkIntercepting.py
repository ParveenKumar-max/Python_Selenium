# Network Intercepting Request & Response

from playwright.sync_api import Page

fakePayload_Intercept = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(json=fakePayload_Intercept)


#-> api call from browser-> api call contact server return back response to browser-> browser use response to generate html
def test_NetworkIntercepting(page:Page):
    page.goto("https://rahulshettyacademy.com/client")

    # Now while Intercepting the network, we have one function "route", and we use * --> accept all request

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    # Enter the login credentials 8882698735
    page.get_by_placeholder("email@example.com").fill("parveendogra2@gmail.com")
    page.locator("#userPassword").fill("Qwerty12345@")
    page.get_by_role("button").click()

    # Order History Page
    page.get_by_role("button", name="ORDERS").click()
    Cart_message = page.locator(".mt-4").text_content()
    print(Cart_message)
