import pytest

# fixture 固件
# @pytest.fixture(scope="session",autouse=False,params=[["zhouy218","136671"],["beifan","beifan123"]],ids=["data1","data2"], name="sql")
# def exe_sql(request):
#     print("before: execute database")
#     yield request.param
#     print("After: close database")

@pytest.fixture(scope="function",autouse=True)
def login():
    print("login")