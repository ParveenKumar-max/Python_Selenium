from selenium.webdriver.common.by import By

from E2E_FrameworkDesign.PageObject.checkout_confirmation import checkout_confirm
from utils.browserUtils import browser_utils


class shopPage(browser_utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Adding Locators
        self.click_shop = (By.CSS_SELECTOR, " a[href*='shop']")
        self.select_item = (By.XPATH, "//div[@class='card h-100']")
        self.clickButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # Actions --> In action we have created different methods for three input types
    def clickshop(self):
        self.driver.find_element(*self.click_shop)

    def selectItems_tocart(self, product_name):
        products = self.driver.find_elements(*self.select_item)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                 product.find_element(By.XPATH, "div/button").click()

    def checkout(self):
        self.driver.find_element(*self.clickButton).click()

        # Define checkout_confirmation page in checkout method under shop Page class
        checkout_confirmation = checkout_confirm(self.driver)
        return checkout_confirmation
