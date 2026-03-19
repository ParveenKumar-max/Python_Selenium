from E2E_PlaywrightPython_Framework.PageObject.dashboard import dashboard


class loginpage:

    def __init__(self, page):
        self.page = page

    def loginNavigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def enter_details(self, userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.locator("#userPassword").fill(userPassword)
        self.page.get_by_role("button").click()
        dashboard_page = dashboard(self.page)
        return dashboard_page