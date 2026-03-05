import pytest
from quick_calc.calculator import Calculator, DivisionByZeroError

@pytest.fixture()
def calc():
    return Calculator()

def test_addition(calc):
    assert calc.add(5, 3) == 8

def test_subtraction(calc):
    assert calc.subtract(10, 4) == 6

def test_multiplication(calc):
    assert calc.multiply(6, 7) == 42

def test_division(calc):
    assert calc.divide(8, 2) == 4

def test_division_by_zero(calc):
    with pytest.raises(DivisionByZeroError):
        calc.divide(5, 0)

def test_negative_numbers(calc):
    assert calc.add(-5, -3) == -8

def test_decimal_numbers(calc):
    assert calc.multiply(2.5, 4) == 10.0

def test_large_numbers(calc):
    big = 10**12
    assert calc.add(big, big) == 2 * big

def test_clear(calc):
    assert calc.clear() == 0
