from paragony import split_price, get_description, format_price
import pytest


def test_pass():
    # asercja podlega sprawdzeniu - czy warunek jest sprawdzony
    assert 2 == 2


# def test_fail():
#     assert 2 > 2


def test_split_price():
    price_zl, price_gr = split_price(100)
    assert price_zl == 1
    assert price_gr == 0


def test_split_price_typical():
    # gdy dziesiątki i zera są niezerowe
    price_zl, price_gr = split_price(123)
    assert price_zl == 1
    assert price_gr == 23


def test_split_price_gr_less_than_10():
    price_zl, price_gr = split_price(101)
    assert price_zl == 1
    assert price_gr == 1


def test_split_price_zl_less_than_1():
    price_zl, price_gr = split_price(15)
    assert price_zl == 0
    assert price_gr == 15


def test_split_price_flaot():
    price_zl, price_gr = split_price(10.15)
    assert price_zl == 0
    assert price_gr == 10


def test_split_price_string_invalid():
    with pytest.raises(ValueError):
        split_price("asdf")


def test_split_price_str_convertable():
    price_zl, price_gr = split_price("10")
    assert price_zl == 0
    assert price_gr == 10


"""
przy testach mozna powatrzac kod
"""


def test_get_description_typical():
    description = get_description("Bananas", 499)
    assert description == "Price of Bananas is 4.99"


def test_get_description_gr_less_than_10():
    description = get_description("Bananas", 801)
    assert description == "Price of Bananas is 8.01"


def test_get_description_zl_less_than_1():
    description = get_description("Bananas", 95)
    assert description == "Price of Bananas is 0.95"


# def test_get_description_empty_name():
#     description = get_description("", 999)
#     assert description == "Price of unknown product is 9.99"


def test_get_description_empty_name():
    # spodziewam sie ze zostanie rzucony wyjątek ValueError
    with pytest.raises(ValueError):
        get_description("", 999)
    with pytest.raises(ValueError):
        get_description(None, 999)


# dopasowaliśmy  test do implementacji, co jest złe.
# nalezy tak myslec co chcemy dostac w wyniku, a
# nie co nam zwroci program


def test_get_description_zero_price():
    description = get_description("Apples", 0)
    assert description == "Price of Apples is 0.00"


def test_get_description_negative_price():
    description = get_description("Apples", -990)
    assert description == "Price of Apples is -9.90"


def test_split_price_negative():
    price_zl, price_gr = split_price(-990)
    assert price_zl == -9
    assert price_gr == 90


def test_format_price_typical():
    assert format_price(1234) == "12.34"


def test_format_price_0zl():
    assert format_price(34) == "0.34"


def test_format_price_0gr():
    assert format_price(5700) == "57.00"


def test_format_price_negative():
    assert format_price(-6785) == "-67.85"


def test_format_price_not_number():
    assert format_price("dupa") == "0.00"
