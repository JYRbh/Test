#读取数据方法
import pytest

def read_yaml():
    return [{'a':'b'},{'a':'c'}]

@pytest.fixture(scope="function",autouse=False,name='login')
def login_ecshop():
    print("登录前")
    yield "登陆成功"
    print("登陆后")

@pytest.fixture(scope="session",autouse=True,name='all')
def all_exe():
    print("all_exe之前")
    yield "登陆成功"
    print("all_exe之后")