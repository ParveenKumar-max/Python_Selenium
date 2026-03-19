from E2E_PlaywrightPython_Framework.PageObject.orderHistory import orderHistory


class dashboard:

    def __init__(self, page):
        self.page = page


    def selectOrderNavigation(self):
        self.page.get_by_role("button",name="ORDERS").click()
        order_history = orderHistory(self.page)
        return order_history
