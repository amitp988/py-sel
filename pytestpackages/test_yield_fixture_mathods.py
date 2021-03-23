import pytest

@pytest.yield_fixture()

def Setup():
    print("Run the setup")
    yield
    print("Run the teardown")
def test_demo_mathodA(Setup):
    print("This is Mathod A")
def test_demo+mathodB(Setup):
    print("This is Mathod B")

