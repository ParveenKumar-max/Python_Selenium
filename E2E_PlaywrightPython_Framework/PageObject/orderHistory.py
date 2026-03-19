from playwright.sync_api import expect

from E2E_PlaywrightPython_Framework.PageObject.orderDetailsSuccess import orderDetailSuccess


class orderHistory:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, OrderID):
        row = self.page.locator("tr").filter(has_text=OrderID)
        row.get_by_role("button", name="View").click()
        order_detail = orderDetailSuccess(self.page)
        return order_detail