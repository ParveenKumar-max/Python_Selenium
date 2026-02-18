# First Playwright Program

from playwright.sync_api import Page

#def test_playwright_basics(playwright):
#    browser = playwright.chromium.launch(headless=False)
#    context = browser.new_context()
#    page = context.new_page()
#   page.goto("https://rahulshettyacademy.com/AutomationPractice/")

#chrominum headless mode , 1  single context, For Firefox , it won't work. 90% used in Projects.
# Change the configuration to --headed
def test_playwright_browser(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")




