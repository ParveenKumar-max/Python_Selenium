import time

from playwright.sync_api import Page, expect


def test_CheckVisibleInvisibleChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.mouse.wheel(0,500)
    time.sleep(5)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)

def test_AlertPopsCheck(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_role("button", name="Alert").click()
    time.sleep(5)
    page.on("dialog" , lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

def test_iframeInOutChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.mouse.wheel(0,1000)
    Page_iframe_Store = page.frame_locator("#courses-iframe")
    Page_iframe_Store.get_by_role("link", name="All Access plan").click()
    Page_iframe_Store.locator("body").is_visible()




















