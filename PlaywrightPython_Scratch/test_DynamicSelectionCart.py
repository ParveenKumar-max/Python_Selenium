import time

from playwright.sync_api import Page, expect


def test_DynamicSelectionCart(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print(page.title())
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Teacher")
    page.get_by_role("checkbox").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)
    selectIphone = page.locator("app-card").filter(has_text="iphone X") #Don't add (.), while adding classes in locators, .add-card,
    selectIphone.get_by_role("button").click()
    selectBlackberry = page.locator("app-card").filter(has_text="Blackberry")
    selectBlackberry.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")







