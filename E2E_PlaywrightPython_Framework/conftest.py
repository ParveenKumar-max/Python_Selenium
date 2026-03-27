# In conftest file we will define our fixture, OR reusable code.
#Fixture we will use to set up and tear down the test script
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="browser selection"
    )

@pytest.fixture(scope='session')
def User_Credentials_data(request):
    return request.param()


@pytest.fixture()
def openbrowser(playwright, request): # With the help of request we can use the local and global variables
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)  # By Default, headless is true
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    page.goto(url_name)
    yield page
    # use playwright wait
    page.wait_for_timeout(5000)
    context.close()
    browser.close()