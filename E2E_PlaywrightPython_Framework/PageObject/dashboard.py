class dashboard:

    def __init__(self, page):
        self.page = page


    def selectOrderNavigation(self):
        self.page.get_by_role("button",name="ORDERS").click()
