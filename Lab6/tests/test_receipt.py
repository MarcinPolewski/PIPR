from receipts.receipt import Receipt
from receipts.receipt_position import ReceiptPosition
from receipts.item import Item
from datetime import date

import pytest

"""
iter

add posioion 

str
"""


def test_iter():
    item1 = Item("Banan", 699)
    item2 = Item("Babeczka", 499)

    position1 = ReceiptPosition(15, item1)
    position2 = ReceiptPosition(7, item2)

    receipt = Receipt([position1, position2])
    receipt_it = iter(receipt)

    assert receipt_it == position1
    next(receipt_it)
    assert receipt_it == position2


# czy to ma sens???
def test_iter_empty_list():
    with pytest.raises(ValueError):
        receipt = Receipt([], date.today())


def test_add_position_existing():
    item1 = Item("Banan", 699)
    item2 = Item("Babeczka", 499)

    position1 = ReceiptPosition(15, item1)
    position2 = ReceiptPosition(7, item2)

    receipt = Receipt([position1, position2])
    receipt.add_position(10, item1)

    new_position = ReceiptPosition(25, item1)

    assert new_position in receipt.positions
    assert position2 in receipt.positions


def test_add_position_new_element():
    item1 = Item("Banan", 699)
    item2 = Item("Babeczka", 499)
    item3 = Item("Mocny Ful", 399)

    position1 = ReceiptPosition(15, item1)
    position2 = ReceiptPosition(7, item2)

    receipt = Receipt([position1, position2])
    receipt.add_position(10, item3)

    assert item1 in receipt.positions
    assert item2 in receipt.positions
    assert item3 in receipt.positions


def test__str__():
    item1 = Item("Banan", 699)
    item2 = Item("Babeczka", 499)

    position1 = ReceiptPosition(15, item1)
    position2 = ReceiptPosition(7, item2)

    receipt = Receipt([position1, position2])
    s = str(receipt)
    assert (
        s
        == f"Wed, 22.11.2023, 00:00:00\n__________________________________________________\n{str(position1)}\n{str(position2)}\n__________________________________________________\nTOTAL: {str(receipt.total_price)}"
    )
