# In conftest file we will define our fixture, OR resuable code.
import pytest


@pytest.fixture(scope='session')
def User_Credentials_data(request):
    return request.param()