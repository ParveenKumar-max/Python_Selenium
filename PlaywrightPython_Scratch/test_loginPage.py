import time

from playwright.sync_api import Page

def test_playwright_LoginPage(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.title()
    page.get_by_label("Username").fill("demo@gmail.com")
    page.get_by_label("Password").fill("Hello@1234")
    page.get_by_role("combobox").select_option("Teacher")
    time.sleep(5)