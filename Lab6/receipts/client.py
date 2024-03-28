from typing import Optional

from .price import Price
from .receipt import Receipt


class Client:
    def __init__(self, name, user_id, receipts: Optional[list[Receipt]] = None):
        pass

    @property
    def name(self):
        pass

    @property
    def user_id(self):
        pass

    @property
    def receipts(self):
        pass

    def add_receipt(self, receipt: Receipt):
        pass

    @property
    def total_spending(self):
        # HINT try to use sum() built-in function here
        # HINT you can also use a list comprehension
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


def random_client() -> Client:
    """Generates a random user"""


def generate_clients(
    num_clients: int, with_receipts=False, num_receipts=10
) -> list[Client]:
    """Generates a given number of fake clients with optional fake receipts"""
