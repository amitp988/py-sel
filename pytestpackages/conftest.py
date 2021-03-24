import pytest

@pytest.yield_fixture()

def setup():
    print("Tis is to run before Mathod")
    yield
    print("This is to run After Mathod")


