import pytest


@pytest.fixture(scope="function",autouse=True,name='pm')
def product_manage():
    print("商品管理之前")
    yield "商品管理"
    print("商品管理之后")