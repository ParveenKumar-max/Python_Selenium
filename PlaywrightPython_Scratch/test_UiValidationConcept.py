import time

import pytest
from playwright.sync_api import Page, expect

#hide/display and placeholder
@pytest.mark.smoke
def test_CheckVisibleInvisibleChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.mouse.wheel(0,500)
    time.sleep(5)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)

#AlertBoxes
@pytest.mark.smoke
def test_AlertPopsCheck(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_role("button", name="Alert").click()
    time.sleep(5)
    page.on("dialog" , lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

#FrameHandling
@pytest.mark.smoke
def test_iframeInOutChecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.mouse.wheel(0,1000)
    Page_iframe_Store = page.frame_locator("#courses-iframe")
    Page_iframe_Store.get_by_role("link", name="All Access plan").click()
    Page_iframe_Store.locator("body").is_visible()

#Check the price of rice is equal to 37.
#identify the price column
#identify rice row
# extract the price of the rice.
@pytest.mark.smoke
def test_HandleWebTables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    Table_Heading = page.locator("th").count()
    print(Table_Heading)
    PriceValueColumn = None
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            PriceValueColumn = index
            print("Price Column Value is : ", PriceValueColumn )
            break
    Rice_Row = page.locator("tr").filter(has_text="Rice")
    expect(Rice_Row.locator("td").nth(PriceValueColumn)).to_have_text("37")

#Same Web Tables login but different approach
@pytest.mark.smoke
def test_HandleWebTables1(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    headers = page.locator("th")
    header_count = headers.count()

    PriceValueColumn = None

    for index in range(header_count):
        if headers.nth(index).inner_text().strip() == "Price":
            PriceValueColumn = index
            print("Price Column Value is:", PriceValueColumn)
            break

    assert PriceValueColumn is not None, "Price column not found"

    Rice_Row = page.locator("tbody tr").filter(has_text="Rice")
    expect(Rice_Row.locator("td").nth(PriceValueColumn)).to_have_text("37")
























