from zadanie1 import Planet
import pytest

"""
moons_number must be integer and cannot be negative 

"""


def test_Planet_init():
    mars = Planet(4, 5, 5, "MaRs")
    assert mars.get_coordinates() == (4, 5, 5)
    assert mars.get_name() == "MaRs"
    assert mars.get_moons_number() == 0


def test_Planet_init_empty_name():
    planet = Planet(5, 4, 2)
    assert planet.get_name() == ""


def test_Planet_init_no_coordinates():
    with pytest.raises(TypeError):
        planet = Planet()


def test_Planet_set_coordinates():
    mars = Planet(4, 5, 5, "MaRs")
    mars.set_coordinates(6, 7, 8)
    assert mars.get_coordinates() == (6, 7, 8)


def test_Planet_set_coordinates_convertable():
    mars = Planet(4, 5, 5, "MaRs")
    mars.set_coordinates("6", 7, "8")
    assert mars.get_coordinates() == (6, 7, 8)


def test_Planet_set_coordinates_not_convertable():
    mars = Planet(4, 5, 5, "MaRs")
    with pytest.raises(ValueError):
        mars.set_coordinates("d", 7, "h")


def test_Planet_set_name():
    mars = Planet(4, 5, 5, "MaRs")
    mars.set_name("baJO Jajjjo")
    assert mars.get_name() == "baJO Jajjjo"


# set_moons_number
def test_Planet_set_moons_number():
    mars = Planet(4, 5, 5, "MaRs")
    mars.set_moons_number(10)
    assert mars.get_moons_number() == 10


def test_Planet_set_moons_number_negaitve():
    mars = Planet(4, 5, 5, "MaRs")
    with pytest.raises(ValueError):
        mars.set_moons_number(-10)


def test_Planet_set_moons_number_float():
    mars = Planet(4, 5, 5, "MaRs")
    mars.set_moons_number(10.0)
    assert mars.get_moons_number() == 10


def test_Planet_set_moons_number_str():
    mars = Planet(4, 5, 5, "MaRs")
    mars.set_moons_number("10")
    assert mars.get_moons_number() == 10
    with pytest.raises(ValueError):
        mars.set_moons_number("test")


def test_Planet__str__():
    mars = Planet(4, 5, 6, "MaRs")
    assert (
        str(mars)
        == "My name is MaRs, i am currently poistioned at (4, 5, 6) and I have 0 moons"
    )
    mars.set_moons_number(10)
    assert (
        str(mars)
        == "My name is MaRs, i am currently poistioned at (4, 5, 6) and I have 10 moons"
    )
