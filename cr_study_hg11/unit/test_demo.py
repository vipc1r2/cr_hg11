import unittest
# 引用unittest

class TestDemo(unittest.TestCase):
# 继承必须用untitest.TestCase
    def fun_1(self) -> str : # -> str 代表，类型提示
        x=None
        return x

    def fun_2(self) :
        x=None
        return x

    # def test_x(self):
    #     demo = TestDemo()
    #     demo.fun_1() # 输入.后会提示出方法
    #     demo.fun_2()  # 输入.后提示，两者有区别，加类型注释系统能推导出来

    @classmethod
    def setUpClass(cls) -> None: # 3.7最新语法 -> None: 类型注解
        print("setupclass")

    def setUp(self) -> None:
        print("setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def tearDown(self) -> None:
        print("tearndown")

    def test_sum(self):
        print("test_sum")
        x = 1 + 2
        print(x)
        self.assertEqual(4, x, f'x={x} expection=3')  # 断言，（期望值，实际值)

    def test_demo(self):
        print("test_demo")
        self.assertTrue(False)


if __name__ == '__main__':  # 运行入口，用终端命令执行如果没有返回值需要加这一行代码
    unittest.main()