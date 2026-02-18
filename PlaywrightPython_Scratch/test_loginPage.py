import time

from playwright.sync_api import Page, Playwright,  expect


def test_playwright_LoginPage(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.title()
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_role("checkbox").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)

# Old password "learning" is no longer valid. Please use the new password "Learning@830$3mK2".

def test_playwright_InvalidCred(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print(page.title())
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("InvalidLearning")
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_role("checkbox").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

# This way we can open OR run the script in the firefox. ByDefault, it will run in chromium.


def test_playwright_Firefox(playwright:Playwright):
    firefoxBrowser = playwright.firefox
    browser = firefoxBrowser.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print(page.title())
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("InvalidLearning")
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_role("checkbox").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

