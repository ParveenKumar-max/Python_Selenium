# The first parameter (self) represents the instance of the class.
# BaseURL --> Core domain URL
# Resources --> that we send to the server.
from playwright.sync_api import Playwright

Order_Details = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
Login_Details = {"userEmail": "parveendogra2@gmail.com", "userPassword": "Qwerty12345@"}

class APIUtils:

    def test_getToken(self, playwright:Playwright):
        api_base_url = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_base_url.post("/api/ecom/auth/login", data=Login_Details)

        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def test_OrderCreater(self, playwright:Playwright):
        token = self.test_getToken(playwright)
        api_base_url = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_base_url.post("/api/ecom/order/create-order",
                            data=Order_Details,
                            headers={"Authorization": token, "Content-Type": "application/json"})

        print(response.json())
        response_body = response.json()
        OrderID = response_body["orders"][0]
        return OrderID



