import pytest
import yaml

from python_code.calc import Calc
from decimal import Decimal

def setup_module():
    print("这是个setup_module方法")

def teardown_module():
    print("这是个teardown_module方法")

class TestCalc:
    def setup_class(self):
        self.calc = Calc()
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    # yaml数据驱动
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("testing.yaml")))
    # @pytest.mark.run(order=-1)
    def test_add1(self, a, b, expect):
        result = self.calc.add(a, b)
        print(f"result = {result}")
        assert result == expect

    # 测试步骤的数据驱动
    def get_steps(self):
        with open('steps.yaml') as f:
            return yaml.safe_load(f)

    def any_steps(self, data, expect):
        steps = self.get_steps()
        for step in steps:
            print(f"step == {step}")
            if 'add' == step:
                assert self.calc.add(*data) == expect
            elif 'add1' == step:
                assert self.calc.add1(data) == expect

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("testing.yaml")))
    # @pytest.mark.run(order=-1)
    def test_add2(self, a, b, expect):
        data = (a, b)
        self.any_steps(data, expect)






        # result1 = self.calc.add(*data)
        # assert result1 == expect
        #
        # result2 = self.calc.add1(data)
        # assert result2 == expect


    # @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("./testing.yaml")))
    # # @pytest.mark.run(order=-1)
    # def select_add1(self, a, b, expect):
    #     result = self.calc.add(a, b)
    #     print(f"result = {result}")
    #     assert result == expect

    # @pytest.mark.run(order=1)
    def test_sub(self):
        assert 1 == self.calc.sub(2, 1)

    # @pytest.mark.run(order=3)
    def test_mul(self):
        assert 6 == self.calc.mul(2, 3)

    # @pytest.mark.run(order=4)
    def test_div1(self):
        result = self.calc.div(1, 1)
        print(f"result = {result}")
        assert result == 1

if __name__ == '__main__':
    pytest.main(['test_calc.py'])


