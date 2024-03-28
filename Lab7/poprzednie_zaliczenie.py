"""
Zaprojektuj i wykonaj klasy reprezentujące przedmiot o masie podanej w kilogramach oraz pojemnik 
(który sam jest przedmiotem) o podanym udźwigu. Przedmioty można wkładać i wyjmować z pojemników, 
o ile są one w ramach dopuszczalnego udźwigu (w przeciwnym razie nie udaje się włożyć przedmiotu do pojemnika). 
Program ma umożliwić wypisanie zawartości każdego pojemnika w postaci zestawu mas przedmiotów, które się w nim znajdują.
"""


class NegativeWeightError(Exception):
    def __init__(self, weight):
        self._weight = weight
        super().__init__(f"weight cannot be negative, {weight} provided")


class OverWeightError(Exception):
    def __init__(self, weight):
        self._weight = weight
        super().__init__(f"weight cannot be negative, {weight} provided")


class Item:
    def __init__(self, name, weight):
        if not name:
            raise ValueError("name cannot be empty")
        weight = int(weight)
        if weight < 0:
            raise NegativeWeightError(weight)

        self._weight = weight
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    def set_name(self, new_name):
        if not new_name:
            raise ValueError("name cannot be empty")
        self._name = new_name

    def set_weight(self, new_weight):
        new_weight = int(new_weight)
        if new_weight < 0:
            raise NegativeWeightError(new_weight)

        self._weight = new_weight

    def __str__(self):
        return self.name


class Box(Item):
    def __init__(self, name, weight, weight_capacity, contents=None):
        weight_capacity = int(weight_capacity)
        if weight_capacity < 0:
            raise NegativeWeightError(weight_capacity)
        self._weight_capacity = weight_capacity

        if not contents:
            contents = []
        self._contents = contents

        if self.current_load > self.weight_capacity:
            raise OverWeightError(self.current_load)

        super().__init__(name, weight)

    @property
    def contents(self):
        return self._contents

    @property
    def weight_capacity(self):
        return self._weight_capacity

    @property
    def current_load(self):
        return sum([item.weight for item in self._contents])

    def add_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("item is not an instance of Item class")
        if self.current_load + item.weight > self.weight_capacity:
            raise OverWeightError(self.current_load + item.weight)
        self._contents.append(item)

    def __str__(self):
        # text = str([str(element) + ", " for element in self.contents])
        # text = text[:-2]
        text = ""
        for element in self.contents:
            text += str(element) + ", "
        text = text[:-2]
        return f"This is {self.name} box, it contains {text} with current load of {self.current_load}kg"

    # jak zrobić eby działało
