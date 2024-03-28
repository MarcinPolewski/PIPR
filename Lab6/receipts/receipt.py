from typing import Optional

from .item import Item
from .price import Price
from .receipt_position import ReceiptPosition


class Receipt:
    def __init__(self, positions: Optional[list[ReceiptPosition]] = None):
        # set date attribute and set it to today
        # https://docs.python.org/3/library/datetime.html
        pass

    @property
    def date(self):
        pass

    @property
    def positions(self):
        pass

    @property
    def total_price(self) -> Price:
        # HINT try to use sum() built-in function here
        # HINT you can also use a list comprehension
        pass

    def __iter__(self):
        # HINT this will allow you to write `for position in receipt:`
        # HINT you simply want to return the iterator over `positions`
        pass

    def __len__(self):
        # HINT this will allow you to write `len(receipt)`
        # HINT the length of the receipt is the number of positions
        pass

    def top_expensive_positions(self, num_positions=1):
        # HINT try sorting positions by their total price
        # HINT https://docs.python.org/3/howto/sorting.html
        pass

    def add_position(self, amount: float, item: Item):
        pass

    def __repr__(self):
        pass

    def __str__(self) -> str:
        # FIXME this is hacky but simple and not super important
        result = f"{self.date.strftime('%a, %d.%m.%Y, %H:%M:%S')}\n"
        separator = "-" * 50 + "\n"
        result += separator
        for position in self.positions:
            result += str(position)
        result += separator
        total_price = f"TOTAL: {self.total_price!s}"
        result += f"{total_price:>{len(separator) - 1}}\n"
        return result


def random_receipt() -> Receipt:
    """Generates a random receipt"""


def generate_receipts(num_receipts: int) -> list[Receipt]:
    """Generates a given number of fake receipts"""
