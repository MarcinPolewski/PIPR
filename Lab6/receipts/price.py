from __future__ import annotations


class Price:
    def __init__(self, value_gr):
        pass

    @property
    def value_gr(self):
        pass

    def __add__(self, other: Price) -> Price:
        # HINT https://docs.python.org/3/library/operator.html
        pass

    def __sub__(self, other: Price) -> Price:
        pass

    def __mul__(self, multiplier: float) -> Price:
        pass

    def __rmul__(self, multiplier: float) -> Price:
        pass

    def __lt__(self, other: Price):
        # HINT this should allow sorting Prices by value_gr
        pass

    @classmethod
    def from_float(cls, value: float) -> Price:
        # HINT this will be called `p = Price.from_float(1.25)`
        # HINT we expect it to work like `p = Price(125)`
        # HINT notice cls instead of self!
        # HINT `cls(125)` will be `Price(125)` in this case!
        # HINT try using the round() built-in function
        pass

    def _split_price(self) -> tuple[int, int]:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        # repr is a raw description of the instance
        # usually you implement it like this:
        return f"{self.__class__.__name__}(value_gr={self.value_gr})"

    def _format_price(self):
        # HINT zl, gr = self._split_price()
        pass

    def __eq__(self, other) -> bool:
        pass


def random_price() -> Price:
    """Generates a random Price object"""


def generate_prices(num_prices: int) -> list[Price]:
    """Generates a given number of random items"""
