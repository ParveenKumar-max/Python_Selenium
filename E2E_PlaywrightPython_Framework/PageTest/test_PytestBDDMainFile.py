import os
import pytest
from pytest_bdd import given, when, then, scenarios, parsers


from E2E_PlaywrightPython_Framework.PageObject.login import loginpage
from E2E_PlaywrightPython_Framework.Utils.Base_WebAPI_PlaywrightPython import APIUtils

# ✅ Dynamic path — works on all machines
scenarios(os.path.join(os.path.dirname(__file__), '../features/orderTransaction.feature'))


@pytest.fixture
def shared_data():
    return {}


# ✅ parsers.parse() used + step text matches feature file exactly
@given(parsers.parse('Enter the {Username} and {Password} and place the order'))
def credentials_place_order(playwright, Username, Password, shared_data):
    user_credentials = {
        "userEmail": Username,
        "userPassword": Password
    }
    apiutils = APIUtils()
    OrderID = apiutils.test_OrderCreator(playwright, user_credentials)
    assert OrderID is not None, "Order creation failed — OrderID is None"
    shared_data["order_id"] = OrderID


# ✅ parsers.parse() used + step text matches feature file exactly
@when(parsers.parse('I logged with {Username} and {Password} in portal'))
def user_in_landing_page(openbrowser, Username, Password, shared_data):
    login_page = loginpage(openbrowser)
    login_page.loginNavigate()
    dashboard_page = login_page.enter_details(Username, Password)
    assert dashboard_page is not None, "Login failed — dashboard_page is None"
    shared_data["dashboard"] = dashboard_page


@when("Navigate to the Order page")
def mov_to_order_page(shared_data):
    dashboard_page = shared_data["dashboard"]
    order_history = dashboard_page.selectOrderNavigation()
    assert order_history is not None, "Navigation failed — order_history is None"
    shared_data["orderhistory"] = order_history


@then("Select the Order and fill all the required details")
def fill_the_required_details(shared_data):
    order_history = shared_data["orderhistory"]
    OrderID = shared_data["order_id"]
    order_detail_success = order_history.selectOrder(OrderID)
    assert order_detail_success is not None, "Order selection failed"
    shared_data["orderdetailPage"] = order_detail_success


@then("Order Success message is successfully displayed on page")
def success_page(shared_data):
    order_detail_success = shared_data["orderdetailPage"]
    order_detail_success.orderDetail()



