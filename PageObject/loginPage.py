from selenium.webdriver.common.by import By


class loginPage():
    def __init__(self, driver):  # Create Constructor
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
