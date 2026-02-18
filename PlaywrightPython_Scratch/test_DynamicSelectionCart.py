
from playwright.sync_api import Page

def test_DynamicSelectionCart(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.title()
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_role("checkbox").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
