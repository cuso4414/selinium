import pytest

def test_a():
    print("test_a")
    
class TestDemo():
    def test_a(self):
        print("开始执行 test_a方法")
        x = 'this'
        assert 'h' in x

    def test_b(self):
        print("开始执行 test_b方法")
        x = 'hello'
        assert 'e' in x

    def test_c(self):
        print("开始执行 test_c方法")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__=='__main__':
    pytest.main()
    # pytest.main("-v -x TestDemo")
    # pytest.main(['-v', '-s', 'TestDemo'])
