from cheapcalc_tools import add, subtract, multiply, divide
from pytest import approx


def test_add_typical():
    assert add(23, 45) == 68


def test_add_negative():
    assert add(-10, -15) == -25


def test_add_float():
    assert add(1.0, 2.0) == 3.0


def test_add_negative_float():
    assert add(-1.0, -2.0) == -3.0


def test_add_one_int_one_float():
    assert add(1.0, 2.0) == 3.0


def test_add_not_integers():
    assert add(1.5, 2.7) == 4.2


def test_add_not_integere_and_integer():
    assert add(1.5, 5) == 6.5


# subtract
def test_subtract_typical():
    assert subtract(20, 45) == -25


def test_subtract_negative():
    assert subtract(-10, -15) == 5


def test_subtract_float():
    assert subtract(1.0, 2.0) == -1.0


def test_subtract_negative_float():
    assert subtract(-1.0, -2.0) == 1.0


def test_subtract_one_int_one_float():
    assert subtract(1.0, -2.0) == 3.0


def test_subtract_not_integer():
    assert subtract(4.8, 2.7) == approx(2.1)


def test_subtract_integer_and_no_integer():
    assert subtract(2, 1.7) == approx(0.3)


# multiply
def test_multiply_typical():
    assert multiply(5, 6) == 30


def test_multiply_two_floats():
    assert multiply(5.0, 3.0) == 15.0


def test_multiply_float_and_integer():
    assert multiply(3.4, 2) == 6.8


def test_multiply_not_integer_floats():
    assert multiply(1.2, 1.2) == 1.44


# divide
def test_divide_typical():
    assert divide(20, 4) == 5
    assert divide(4, -2) == -2


def test_divide_two_floats():
    assert divide(0.1604664, 0.68) == 0.23598


def test_divide_float_and_integer():
    assert divide(3.4, 2) == 1.7


def test_divide_not_integer_floats():
    assert divide(-1.2, -1.2) == 1


def test_divide_okresowe():
    assert divide(1, 3) == approx(0.333333333)
