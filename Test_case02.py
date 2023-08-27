import unittest
from parameterized import parameterized


def a(b, c):
    return b % c


# def setUpModule():
#     print("模块级Fixture执行")
#
#
# def tearDownModule():
#     print("模块级Fixture销毁")

# list=[(11,10,1),(12,10,2)]
class test(unittest.TestCase):
    # def setUp(self) -> None:
    #     print("方法级Fixture执行")
    #
    # def tearDown(self) -> None:
    #     print("方法级Fixture销毁")
    #
    # @ classmethod
    # def setUpClass(cls) -> None:
    #     print("类级Fixture执行")
    #
    # @ classmethod
    # def tearDownClass(cls) -> None:
    #     print("类级Fixture销毁")
    @parameterized.expand([(11, 10, 1), (12, 10, 2)])
    def test_01(self, b, c, exp):
        res = a(b, c)
        # 判断101%100的结果是不是Ture
        # self.assertTrue(a(101, 100))

        # 判断101%100的结果是不是False
        # self.assertFalse(a(101, 100))

        # 判断101%100的结果等于1的话，通过
        self.assertEqual(res, exp)

        # 判断101%100的结果不等于2的话，通过
        # self.assertNotEqual(2, a(101, 100))

        # 验证101%100的结果是不是None,是None则pass,不是None则断言失败
        # self.assertIsNone(a(101,100))

        # 验证101%100的结果是不是None,不是None则pass,是None则断言失败
        # self.assertIsNotNone(a(101,100))

        # 判断"1"是否在123中(第二个参数为容器类型)
        # self.assertIn("1",[123,"1"])

        # 判断[123]中是否不存在"1"
        # self.assertNotIn("1",[123])
    # def test_02(self):
    #     print(a(102, 100))
    #
    # def test_03(self):
    #     print(a(103, 100))
    #
    # def test_04(self):
    #     print(a(104, 100))
    #
    # def test_05(self):
    #     print(a(105, 100))
