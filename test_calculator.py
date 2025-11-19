import pytest
from calc import addition, subtraction, division, exponent, multiplication


def test_add_positive_numbers():
    assert addition (5,3) == 8
    assert addition (1051,314098) == 315149
    assert addition (124,641) == 765
def test_add_negative_numbers():
    assert addition (-12,-12) == -24
    assert addition (-2,-5) == -7
def test_add_positive_and_negative_numbers():
    assert addition (5,-2) == 3
    assert addition (-5,10) == 5
    assert addition (-12,7) == -5
def test_add_decimal_numbers():
    assert addition (1.2,1) == 2.2
    assert addition (61.43,93.1) == 154.53
def test_add_negative_decimal_numbers():
    assert addition (-1.5,.5) == -1


def test_subtract_positive_positive():
    assert subtraction (10,5) == 5
    assert subtraction (193,51) == 142
def test_subtract_to_negative():
    assert subtraction (5,10) == -5
    assert subtraction (999,1000) == -1
def test_subtract_negatives():
    assert subtraction (5,-5) == 10
    assert subtraction (-5,5) == -10
def test_subtract_decimals():
    assert subtraction (5.5,1.2) == 4.3


def test_multiply_positive_numbers():
    assert multiplication(5, 3) == 15
    assert multiplication(10, 20) == 200
    assert multiplication(7, 8) == 56
def test_multiply_negative_numbers():
    assert multiplication(-5, -3) == 15
    assert multiplication(-10, -2) == 20
def test_multiply_positive_and_negative_numbers():
    assert multiplication(5, -2) == -10
    assert multiplication(-5, 3) == -15
    assert multiplication(-12, 0.5) == -6
def test_multiply_decimal_numbers():
    assert multiplication(1.5, 2) == 3.0
    assert multiplication(2.5, 0.4) == 1.0
    assert multiplication(0.1, 0.1) == 0.01


def test_divide_positive_numbers():
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(100, 4) == 25
def test_divide_negative_numbers():
    assert division(-10, -2) == 5
    assert division(-9, -3) == 3
def test_divide_positive_and_negative_numbers():
    assert division(10, -2) == -5
    assert division(-10, 2) == -5
def test_divide_decimal_numbers():
    assert division(1.5, 0.5) == 3.0
    assert division(2.4, 0.8) == 3.0
    assert division(0.9, 0.3) == 3.0
def test_divide_by_zero():
    assert division(10,0) == False
def test_divide_zero():
    assert division(0,10) == 0


def test_exponent_positive_numbers():
    assert exponent(2, 3) == 8
    assert exponent(5, 2) == 25
    assert exponent(10, 0) == 1
def test_exponent_negative_numbers():
    assert exponent(-2, 3) == -8
    assert exponent(-2, 2) == 4
def test_exponent_with_decimals():
    assert exponent(4, 0.5) == 2
    assert exponent(9, 0.5) == 3
    assert exponent(2.5, 2) == 6.25
def test_exponent_with_negative_exponent():
    assert exponent(2, -1) == 0.5
    assert exponent(4, -2) == 0.0625
def test_exponent_zero_base():
    assert exponent(0, 5) == 0
    assert exponent(0, 0) == 1
def test_exponent_power_of_0():
    assert exponent(113905813,0) == 1

