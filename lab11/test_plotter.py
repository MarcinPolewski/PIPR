from plotter import sort_recipes


def test_sort_recipes():
    keys = [1, 4, 2, 3]
    vals = ["d", "a", "c", "b"]
    keys, vals = sort_recipes(keys, vals)
    assert list(vals) == ["a", "b", "c", "d"]
