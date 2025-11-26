import pytest


@pytest.mark.usefixtures("dataload")
class TestExample_01:

    def test_editProfile(self, dataload):
        print(dataload)
        print(dataload[0])
        print(dataload[2])