# Move the fixtures in one common file, For reusability and accessible foe every file.
import pytest


@pytest.fixture(scope="class")
def SetUp():
    print(" Fixture will run first")
    yield
    print("Tear down the test")

@pytest.fixture()
def dataload():
    print("User profile is being created.")
    return ["Parveen","Chaudhary","Sap Homes Flat 105, 27LPA"]


@pytest.fixture(params=["Chrome","Firefox","IE"])
def crossbrowser0(request):
    return request.param


@pytest.fixture(params=[("Chrome","Parveen","Chaudhary"),"Firefox","IE"])
def crossbrowser1(request):
    return request.param


@pytest.fixture(params=[("Chrome","Parveen","Chaudhary"),("Firefox","Pintu","Dogra"),("IE","Chaudhary")])
def crossbrowser2(request):
    return request.param

