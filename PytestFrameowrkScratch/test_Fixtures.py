# Fixtures -- Important in pytest testing framework for set up and tear down the resources needed for test

import pytest

@pytest.mark.usefixtures("SetUp")
class TestFirstClass:

    def test_checkFixtures(Self):
        print("Fixture concept checking")

    def test_value(Self):
        S1 = "GeeskForGeeks"
        S2 = lambda func : func.upper()
        print(S2(S1))