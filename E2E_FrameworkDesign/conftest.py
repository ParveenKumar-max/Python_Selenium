import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service



# Predefined function used to call browser from terminal request.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="run slow tests"
    )


@pytest.fixture(scope="session")
def browserInstance(request):
    global driver
    # pick the browser what we ask in terminal  " pytest test_E2EFrameworkDesign.py --browser_name chrome "
    browser_name = request.config.getoption("browser_name")

    if browser_name  == "edge":
        service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")
        driver = webdriver.Edge(service=service_object)
    elif browser_name =="chrome":
        service_object = Service("C:/Users/Default/Documents/chromedriver.exe")
        driver = webdriver.Chrome(service=service_object)
    else:
        raise ValueError("Invalid --browser_name provided. Use chrome or edge.")

    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver   # Before test function execution
    driver.close()  # Post your test function execution