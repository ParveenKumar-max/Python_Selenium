# Move the fixtures in one common file, For reusability and accessible foe every file.
import pytest


@pytest.fixture(scope="class")
def SetUp():
    print(" Fixture will run first")
    yield
    print("Tear down the test")
