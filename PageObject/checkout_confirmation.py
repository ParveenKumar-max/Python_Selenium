from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class checkout_confirm():
        def __init__(self, driver):
            self.driver = driver

# Locators of Checkout and Confirmation Page
            self.successbtn = (By.XPATH, "//button[@class='btn btn-success']")
            self.selectid = (By.XPATH, "//input[@id='country']")
            self.inputINDIA = (By.LINK_TEXT, "India")
            self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
            self.submit = (By.CSS_SELECTOR, "[type='submit']")
            self.successMsg = (By.CLASS_NAME, "alert-success")

# functions or method for adding variables ( dynamic )
        def checkout(self):
                self.driver.find_element(*self.successbtn).click()

        def delivery_address(self, countryName):
                self.wait = WebDriverWait(self.driver, 10)
                self.driver.find_element(*self.selectid).send_keys(countryName)
                self.wait = WebDriverWait(self.driver, 10)
                self.wait.until(expected_conditions.presence_of_element_located(self.inputINDIA))
                self.driver.find_element(*self.inputINDIA).click()

        def last_validation(self):
                self.driver.find_element(self.checkbox).click()
                self.driver.find_element(self.submit).click()
                successText =  self.driver.find_element(self.successMsg).text
                assert "Success! Thank you!" in successText












