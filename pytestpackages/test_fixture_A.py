import pytest
@pytest.fixture()
def setup():
    print("Run it before method")

def test_methodA(setup):
    print("Run test method A")

def test_methodB(setup):
    print("Run test method B")

