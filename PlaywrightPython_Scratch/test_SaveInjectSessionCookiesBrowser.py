# In this file, we save & inject the session & cookies in the browser at run time.
import time

import pytest
from playwright.sync_api import Playwright, expect

from PlaywrightPython_Scratch.utils.Base_Web_APi_Flow import APIUtils

@pytest.mark.smoke
def test_session_storage(playwright: Playwright):
    Get_api = APIUtils()
    getToken = Get_api.test_getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #Script to inject the token in the session local storage, put javascript here
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
    time.sleep(5)
