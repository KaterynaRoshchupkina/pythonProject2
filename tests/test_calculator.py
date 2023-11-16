import pytest
from src.calculator import calculator_function

# 8 тестов на основные функции калькулятора

def test_addition():
    result = calculator_function('+', 3, 4)
    assert result == 7


def test_subtraction():
    result = calculator_function('-', 5, 2)
    assert result == 3


def test_multiplication():
    result = calculator_function('*', 2, 6)
    assert result == 12


def test_division():
    result = calculator_function('/', 8, 2)
    assert result == 4


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calculator_function('/', 5, 0)


def test_square_root():
    result = calculator_function('sqrt', 9, 16)
    assert result == 3


def test_square_root_of_negative_number():
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number!"):
        calculator_function('sqrt', -4, -5)


def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation!"):
        calculator_function('unknown', 2, 3)
