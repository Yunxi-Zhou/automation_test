import pytest

# fixture 固件
@pytest.fixture(scope="session",autouse=True)
def exe_sql():
    print("before: execute database")
    yield
    print("After: close database")
