import pytest

@pytest.mark.usefixtures("pre_post_action","obj")
def test_add(pre_post_action,obj):
    result = 100
    assert obj.add(50,50) == result, "Test for addition is failed"

def test_sub(pre_post_action,obj):
    result = 100
    assert obj.sub(300,200) == result, "Test for subtraction is failed"

def test_mul(pre_post_action,obj):
    result = 100
    assert obj.mul(10,10) == result, "Test for Multiplication is failed"

def test_div(pre_post_action,obj):
    result = 100
    assert obj.div(1000,10) == result, "Test for division is failed"

@pytest.mark.smoke
def test_basic():
    print("System is up and running fine")

@pytest.mark.xfail
def test_mandatorytest():
    print("This is will run for sure")



