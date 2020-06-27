'''
情景1：登录之后验证购物车的功能点
情景2：不登陆的时候购物车的功能点
'''
import pytest


@pytest.fixture
def login():
    print("登陆操作")
    username = 'jerry'
    # return username
    yield username
    print("清空登陆操作")

class TestCart:
    def setup(self):
        print("登陆")

    def test_card1(self, login):

        print(f"test_card1需要登陆，登陆名为：{login}")

    def test_card2(self, login):
        print(f"test_card2需要登陆,登陆名为")

    def test_card3(self):
        print("test_card3不需要登陆")

    def test_card4(self):
        print("test_card4不需要登陆")