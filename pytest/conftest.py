import pytest
from calculator import Calculator

@pytest.fixture
def pre_post_action():
    print("\n Doing action pre TC execution")
    yield
    print("\n Doing action post TC execution \n")

@pytest.fixture
def obj():
    obj = Calculator()
    return obj

@pytest.fixture
def data_load():
    print("I am sending prerequisit data")
    return ["Basant","Joshi","MCA","Jodhpur"]

@pytest.fixture(params=[("Chrome",123),("FireFox",456),("Mozilla",789),("IE",6754)])
def crossBrowser(request):
    return request.param
