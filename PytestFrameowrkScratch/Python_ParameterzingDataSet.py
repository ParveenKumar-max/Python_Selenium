import pytest


#@pytest.mark.usefixtures            We will not add any use fixtures we are already calling it main conftest file.
def test_crossBrowser(crossbrowser0):
    print(f"Test Data:", crossbrowser0)


def test_crossBorwser01(crossbrowser1):
    print(f"Test Data:", crossbrowser1)


def test_crossBorwser02(crossbrowser2):
    print(f"Test Data:", crossbrowser2[1])