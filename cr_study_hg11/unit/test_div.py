import json

import pytest

from cr_study_hg11.unit.div import div

# 利用测试用例分组
@pytest.mark.happy
def test_div_int():
    assert div(10, 2) == 5
    assert div(10, 5) == 3
    assert div(1000000000, 1) == 1000000000
    # 缺点就是一个报错，后续断言不执行了


@pytest.mark.happy
@pytest.mark.parametrize("number1, number2, expection", {
    (10, 2, 5),
    (10, 5, 3),
    (1000000000, 1, 1000000000),
    (100, 200, 0.5)
}) # 参数化（）中参数是变化的，命名参数名字，{(,,),(,,)}数据填充，参数化好处一个case失败不影响其他case
def test_div_int_param(number1, number2, expection):
    assert div(number1, number2) == expection

# 参数化读取json文件来获得参数,利用json存储数据，需要结构化一定语法要求
# @pytest.mark.happy
# @pytest.mark.parametrize("number1, number2, expection", json.load('1.json'))
# def test_div_int_ddd(number1, number2, expection):
#     assert div(number1, number2) == expection

@pytest.mark.happy
def test_div_float():
    assert div(10, 3) == 3.33333333
    assert div(10.2, 0.2) == 51

@pytest.mark.exception
def test_div_exception():
    assert div(10, 'a')
    assert div('abc', 10)

@pytest.mark.exception
def test_div_zero():
    assert div(10, 0) == None