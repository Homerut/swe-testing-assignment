from quick_calc.calculator import Calculator
import pytest

calc = Calculator()

def test_integration_addition():
    assert calc.add(5,3) == 8

def test_integration_subtraction():
    assert calc.subtract(10,4) == 6
