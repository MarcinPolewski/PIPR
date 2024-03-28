from zadanie2 import calculate_distance_one_dimension


def test_distance_one_dimension_typical():
    assert calculate_distance_one_dimension(4, 2, 3) == 1


def test_distance_one_dimension_same_point():
    assert calculate_distance_one_dimension(4, 2, 2) == 0


def test_distance_one_dimension_both_sides_same_number():
    assert calculate_distance_one_dimension(4, 1, -1) == 2


def test_distance_one_dimension_both_sides():
    assert calculate_distance_one_dimension(4, 2, -1) == 3


def test_distance_one_dimension_around():
    assert calculate_distance_one_dimension(4, 4, -3) == 2
