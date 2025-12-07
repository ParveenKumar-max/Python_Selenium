# test file should start with test_ or end with _test ( And It's Mandatory )
# Any function or method define in test file should start with test like ( test_FirstTest )
# Any code should be wrapped in the method only
# Every method treat as a separate testcase
# Method name should have some sense
# -k stands for method name execution, -s stand for logs in out, -v stand for more info metadata
# you can mark ( tag ) "smoke" and then run with -m, py.test -m smoke -v -s
import pytest


#@pytest.mark.smoke
@pytest.mark.skip
def test_FirstProgram():
    print("Hello First Pytest Framework Program")

def test_int():
    x = 1
    result = x + 1
    assert result == 2
    print(result)

@pytest.mark.xfail
def test_SecondProgram():
    print("Hello First Pytest Framework Program")