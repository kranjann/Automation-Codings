import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstFunction():
    message = "hello partTwo"
    assert message == "Hi"

def test_secondCreditFuntion():
    a = 4
    b = 6
    assert a+2 == 6, "This is not true"

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")