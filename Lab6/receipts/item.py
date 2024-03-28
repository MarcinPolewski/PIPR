from .price import Price

BARCODE_LENGTH = 13


class Item:
    def __init__(self, name, price: Price, barcode: str = "1234567890123"):
        # HINT barcode must be valid and have 13 digits
        pass

    @property
    def name(self):
        pass

    @property
    def price(self):
        pass

    @property
    def barcode(self):
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass


def random_item() -> Item:
    """Generate a random item"""


def generate_items(num_items: int) -> list[Item]:
    """Generates a given number of random items"""
