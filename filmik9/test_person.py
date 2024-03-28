from model import Person
from model import InvalidSexError, InvalidNameError

from datetime import date
import pytest


def test_Person_init():
    bd = date(year=1994, month=5, day=4)

    person1 = Person(id=5, name="Jórek Ogórek", sex="Male", birth_date=bd)
    assert person1.sex == "Male"
    assert person1.id == 5
    assert person1.name == "Jórek Ogórek"
    assert person1.birth_date == bd


def test_Person__str__():
    bd = date(year=1994, month=5, day=4)
    person1 = Person(id=5, name="Jórek Ogórek", sex="Male", birth_date=bd)

    assert str(person1) == "Jórek Ogórek"


def test_Person_init_invalid_arguments():
    bd = date(year=1994, month=5, day=4)
    with pytest.raises(InvalidNameError):
        person1 = Person(id=5, name="", sex="Male", birth_date=bd)
    with pytest.raises(InvalidSexError):
        person1 = Person(id=5, name="Jórek Ogórek", sex="aksdf", birth_date=bd)
