'''
python unittest 测试框架
'''
import unittest

class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup calss")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")
        self.assertIn('h', 'this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1, 1, "判断相等")
        # self.assertIn('h', 'this')

    @unittest.skipIf(1+1 == 2, "跳过这条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3, 4, "判断相等")
        # self.assertIn('h', 'this')

class demo1(unittest.TestCase):
    def test_demo01_case0(self):
        print("test_demo01 case0")

    def test_demo01_case1(self):
        print("test_demo01 case1")

class demo2(unittest.TestCase):
    def test_demo02_case0(self):
        print("test_demo02 case0")

    def test_demo02_case1(self):
        print("test_demo02 case1")


if __name__ == '__main__':
    # 执行方式1
    # unittest.main()

    # 执行方式2
    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_demo01_case0"))

    # unittest.TextTestRunner().run(suite)

    # 执行方式3
    # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite, suite1])
    # unittest.TextTestRunner().run(suiteall)

    # 执行方式4
    discover = unittest.defaultTestLoader.discover("./", 'test*.py')
    unittest.TextTestRunner().run(discover)