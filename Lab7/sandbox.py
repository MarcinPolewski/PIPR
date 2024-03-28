class Foo:
    def __init__(self, numbers=[]):
        self._numbers = numbers

    def add_number(self, number):
        self._numbers.append(number)


if __name__ == "__main__":
    bar = Foo()
    baz = Foo()
    bar.add_number(7)
    baz.add_number(8)

    # bar i baz mają w sobie elementy 7 i 8
    # wszystkie obiekty Foo, które nie podają listy, mają tą samą listę
    # w pythonie nie powinno się podawać list jako argument domysłny
    # obchodzic to przez none


class Foo:
    def __init__(self, numbers=None):
        self._numbers = numbers if numbers is not None else []
        # jeśli numbers jest pusta, to zostanie stworzona nowa lista


if __name__ == "__main__":
    bar = Foo()
    baz = Foo()
    bar.add_number(7)
    baz.add_number(8)
