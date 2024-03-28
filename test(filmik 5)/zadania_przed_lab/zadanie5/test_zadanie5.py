import zadanie5


def test_calculate_avg_typical():
    assert zadanie5.calculate_avg([1, 2, 3]) == 2
    assert zadanie5.calculate_avg([10, 5, 15]) == 10


def test_calculate_avg_one_element():
    assert zadanie5.calculate_avg([5]) == 5


def test_calculate_avg_same_element():
    assert zadanie5.calculate_avg([5, 5, 5, 5]) == 5


def test_calculate_avg_all_negative():
    assert zadanie5.calculate_avg([-1, -2, -3]) == -2


def test_calculate_avg_mixed_signs():
    assert zadanie5.calculate_avg([-5, 0, 5]) == 0


def test_count_elements_above_average_typical():
    assert zadanie5.count_elements_above_average([1, 2, 3]) == 1
    assert zadanie5.count_elements_above_average([3, 2, 1]) == 1


def test_count_elements_above_average_equal_elements():
    assert zadanie5.count_elements_above_average([1, 1, 1]) == 0


def test_count_elements_for_arrays_typical():
    assert zadanie5.count_elements_for_arrays([[1, 2, 3], [4, 5, 6]]) == [1, 1]


def test_count_elements_for_arrays_all_negative():
    assert zadanie5.count_elements_for_arrays([[-1, -2, -3], [-4, -5, -6]]) == [1, 1]


def test_count_elements_for_arrays_mixed_symbols():
    assert zadanie5.count_elements_for_arrays([[-1, 0, 1]]) == [1]


def test_count_elements_for_arrays_empty_element():
    assert zadanie5.count_elements_for_arrays(
        [[1, 2, 3], [5, 6, 7], [], [3, 4, 5]]
    ) == [1, 1, "DZIELENIE PRZEZ ZERO", 1]


def test_count_elements_for_arrays_non_convertable_value():
    assert zadanie5.count_elements_for_arrays(
        [[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ["12a", 1, 4]]
    ) == [1, 1, "DZIELENIE PRZEZ ZERO", 1, "ZŁA WARTOŚĆ"]


def test_count_elements_for_arrays_convertable_value():
    assert zadanie5.count_elements_for_arrays(
        [[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ["1", 2, 3]]
    ) == [1, 1, "DZIELENIE PRZEZ ZERO", 1, 1]
