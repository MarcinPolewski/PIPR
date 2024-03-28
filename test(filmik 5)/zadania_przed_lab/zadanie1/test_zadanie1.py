from zadanie1 import find_max_sum
import pytest


def test_find_max_sum_typical():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert find_max_sum(a, 3) == (7, 27)
    assert find_max_sum(a, 1) == (9, 10)


def test_find_max_sum_negative():
    a = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    assert find_max_sum(a, 2) == (0, -3)
    assert find_max_sum(a, 1) == (0, -1)
    assert find_max_sum(a, 3) == (0, -6)


def test_find_max_sum_subsequence_longer_than_sequence():
    # w takie sytuacji zwrócić błąd
    # nie mozna wystawic 0, bo nie jestesmy wstanie podac indeksu
    # 0 nie ma sensu bo liczby moga byc ujemne
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with pytest.raises(ValueError):
        find_max_sum(a, 100)


def test_find_max_sum_sequence_is_empty():
    # rzucić ValueError
    a = []
    with pytest.raises(ValueError):
        find_max_sum(a, 100)


def test_find_max_sum_sequence_is_constant():
    a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert find_max_sum(a, 2) == (0, 2)
    assert find_max_sum(a, 5) == (0, 5)


def test_find_max_sum_subsequence_len_zero():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with pytest.raises(ValueError):
        find_max_sum(a, 0)
