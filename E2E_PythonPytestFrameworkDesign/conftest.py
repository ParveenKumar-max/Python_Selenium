import os

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service


# Predefined function used to call browser from terminal request.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or edge",
    )

# Initialize driver and Call browser
@pytest.fixture(scope="session")
def browserInstance(request):
    global driver

    # pick the browser what we ask in terminal  " pytest test_E2EFrameworkDesign.py --browser_name chrome "
    browser_name = request.config.getoption("browser_name")

    if browser_name  == "edge":
        options = webdriver.EdgeOptions()       # option class we used to capture the logs
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

        service_object = Service("C:/Users/Default/Documents/msedgedriver.exe")
        driver = webdriver.Edge(service=service_object, options=options)

    elif browser_name =="chrome":
        options = webdriver.ChromeOptions()    # option class we used to capture the logs
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

        service_object = Service("C:/Users/Default/Documents/chromedriver.exe")
        driver = webdriver.Chrome(service=service_object, options=options)
    else:
        raise ValueError("Invalid --browser_name provided. Use chrome or edge.")

    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver   # Before test function execution
    driver.quit()  # Post your test function execution




# set up a hook to be able to check if a test has failed
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when in ("call", "setup") and report.failed:
            # Get the driver from test function
        driver = item.funcargs.get("browserInstance") or item.funcargs.get("driver")

        if driver:
               reports_dir = os.path.join(os.path.dirname( __file__ ), "reports" )
               os.makedirs(reports_dir, exist_ok=True)
                  # Save screenshot
               file_name = report.nodeid.replace( "::", "_" ) + ".png"
               file_path = os.path.join(reports_dir, file_name)

               driver.save_screenshot(file_path)

               html = f"""
               <div>
                     <img src="reports/{file_path}" alt="screenshot" 
                     style="width:304px;height:228px;"
                     'onclick="window.open(this.src)" align="right"/>
               </div>
               """
               extra.append(pytest_html.extras.html(html))

        report.extras = extra

