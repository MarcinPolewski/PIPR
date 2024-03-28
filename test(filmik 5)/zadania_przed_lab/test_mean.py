from plik import mean
import pytest

# Napisz dowolny test sprawdzający funkcję mean​ , załóż, że funkcja przyjmuje na wejściu listę liczb i zwraca ich uśrednioną wartość.


def test_mean_typical():
    assert mean([1, 2, 3]) == 2


def test_mean_one_element():
    assert mean([1]) == 1


def test_mean_different_signs():
    assert mean([-1, 0, 1]) == 0


def test_mean_negative():
    assert mean([-1, -2, -3]) == -2


def test_mean_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean([])
