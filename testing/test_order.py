import pytest

# fixtures documentation order example
order = []

# session 级别的第一个执行
@pytest.fixture(scope="session")
def s1():
    order.append("s1")

# 模块级别，仅次于session
@pytest.fixture(scope ="module")
def m1():
    order.append("m1")


@pytest.fixture
def f1(f3):
    order.append("f1")

# 其余顺序执行，执行f1发现依赖于f3，先执行f3
@pytest.fixture
def f3():
    order.append("f3")

# 没有定义，默认方法级别，autouse优先于同级别其他先执行
@pytest.fixture(autouse=True)
def a1():
    order.append("a1")


@pytest.fixture
def f2():
    order.append("f2")


def test_order(f1, m1, f2, s1):
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]

