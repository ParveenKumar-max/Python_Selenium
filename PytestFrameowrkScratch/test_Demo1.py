# working with method in Pytest Framework
import pytest


def test_string():
    S1 = 2
    S2 = S1
    print(S2 + S1)

@pytest.mark.smoke
def test_print():
    num = 5
    #for i; for 5>1: i+=
    print(num)