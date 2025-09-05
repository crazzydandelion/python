import pytest
from calculator import Calculator
# calculator = Calculator()
# numbers = [1,2,3,4,5,6,7,8,9,5]
# res = calculator.avg(numbers)
# print(res)

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9