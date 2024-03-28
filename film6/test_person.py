from definitions import Person


def test_init():
    person = Person("first", "last")
    assert person.first_name == "first"
    assert person.last_name == "last"


def test_init_with_age():
    person = Person("first", "last", 420)
    assert person.first_name == "first"
    assert person.last_name == "last"
    assert person.age == 420
