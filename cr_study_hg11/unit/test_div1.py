

import pytest

from cr_study_hg11.unit.div import div


def test_div_int():
    assert div(10, 2) == 5
    assert div(10, 5) == 3
    assert div(1000000000, 1) == 1000000000


def test_div_float():
    assert div(10, 3) == 3.33333333
    assert div(10.2, 0.2) == 51


def test_div_exception():
    assert div(10, 'a')
    assert div('abc', 10)


def test_div_zero():
    assert div(10, 0) == None