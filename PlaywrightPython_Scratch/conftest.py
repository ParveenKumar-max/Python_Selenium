import pytest


@pytest.fixture(scope="function")
def preWork():
    print("This will run first")


@pytest.fixture(scope="function")
def preWorkTogether():
    print("This will use second program")