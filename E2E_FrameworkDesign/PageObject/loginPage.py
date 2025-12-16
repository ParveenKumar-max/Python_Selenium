from selenium.webdriver.common.by import By

from E2E_FrameworkDesign.PageObject.ShopPage import shopPage
from utils.browserUtils import browser_utils


class loginPage(browser_utils):
    def __init__(self, driver):  # Create Constructor
        super().__init__(driver)
        self.driver =  driver

 # Locators
        self.username_input = (By.ID,"username")
        self.password_input = (By.NAME,"password")
        self.submit = (By.ID,"signInBtn")


 # Actions --> In action we have created 3 different methods for three input types
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_submit(self):
        self.driver.find_element(*self.submit).click()

# Combined Actions
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.enter_submit()

        # Define Shop page in login method under Login Page class
        shop_page = shopPage(self.driver)
        return shop_page