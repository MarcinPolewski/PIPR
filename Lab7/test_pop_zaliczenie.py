from poprzednie_zaliczenie import Item, Box, NegativeWeightError, OverWeightError
import pytest


def test_Item():
    banana = Item(name="banana", weight=5)
    assert banana.name == "banana"
    assert banana.weight == 5


def test_Item_exceptions():
    with pytest.raises(NegativeWeightError):
        banana = Item(name="banana", weight=-5)
    with pytest.raises(ValueError):
        banana = Item(name="", weight=5)


def test_Box():
    item1 = Item("banan", 5)
    item2 = Item("cola", 2)
    a = [item1, item2]
    box = Box(name="karton", weight=10, weight_capacity=50, contents=a)
    assert box.name == "karton"
    assert box.weight == 10
    assert box.weight_capacity == 50
    assert box.contents == a


def test_Box_no_contents():
    box = Box(name="karton", weight=10, weight_capacity=50)
    assert box.name == "karton"
    assert box.weight == 10
    assert box.weight_capacity == 50


def test_Box_over_weight():
    item1 = Item("banan", 50)
    item2 = Item("cola", 20)
    a = [item1, item2]
    with pytest.raises(OverWeightError):
        box = Box(name="karton", weight=10, weight_capacity=50, contents=a)


def test_Box_NegativeWeightError():
    with pytest.raises(NegativeWeightError):
        box = Box(name="karton", weight=-10, weight_capacity=50)
    with pytest.raises(NegativeWeightError):
        box = Box(name="karton", weight=10, weight_capacity=-50)


def test_Box_current_load():
    item1 = Item("banan", 5)
    item2 = Item("cola", 2)
    a = [item1, item2]
    box = Box(name="karton", weight=10, weight_capacity=50, contents=a)
    assert box.current_load == 7


def test_Box_add_item():
    item1 = Item("banan", 5)
    item2 = Item("cola", 2)
    item3 = Item("Komputer", 4)
    a = [item1, item2]
    box = Box(name="karton", weight=10, weight_capacity=50, contents=a)

    box.add_item(item3)
    assert len(box.contents) == 3
    assert item3 in box.contents
    assert item2 in box.contents
    assert item1 in box.contents


def test_Box_add_item_over_weight():
    item1 = Item("banan", 5)
    item2 = Item("cola", 2)
    item3 = Item("Komputer", 40)
    a = [item1, item2]
    box = Box(name="karton", weight=10, weight_capacity=10, contents=a)

    with pytest.raises(OverWeightError):
        box.add_item(item3)


def test_Box_add_item_over_weight():
    item1 = Item("banan", 5)
    item2 = Item("cola", 2)
    item3 = "orange"
    a = [item1, item2]
    box = Box(name="karton", weight=10, weight_capacity=10, contents=a)

    with pytest.raises(ValueError):
        box.add_item(item3)


def test_Box_add_item_equal_weight():
    item1 = Item("banan", 5)
    item2 = Item("cola", 5)
    item3 = Item("Komputer", 5)
    a = [item1, item2]
    box = Box(name="karton", weight=10, weight_capacity=15, contents=a)

    box.add_item(item3)
    assert len(box.contents) == 3
    assert item3 in box.contents
    assert item2 in box.contents
    assert item1 in box.contents


def test_Box__str__():
    item1 = Item("banana", 5)
    item2 = Item("cola", 5)
    item3 = Item("Komputer", 5)
    a = [item1, item2, item3]
    box = Box(name="karton", weight=10, weight_capacity=15, contents=a)

    box_description = str(box)
    assert (
        box_description
        == "This is karton box, it contains banana, cola, Komputer with current load of 15kg"
    )
