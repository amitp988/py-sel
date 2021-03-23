import pytest
@pytest.yield_fixture()

def setup():
    print("Run before method")
    yield
    print("run after method")

def test_method_C(setup):
    print("This is method c")
    
def test_methos_D(setup):
    print("This is method d")