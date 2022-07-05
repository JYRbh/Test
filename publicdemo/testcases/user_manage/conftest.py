import pytest


@pytest.fixture(scope="function",autouse=True,name='um')
def user_manage():
    print("用户管理模块之前的准备工作")
    yield "user_manage"
    print("用户管理模块之后的扫尾工作")