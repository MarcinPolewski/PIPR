from zadanie2 import Package
import pytest


# sender
# recipient

"""
weight > 0 
dimensions > 0 
sender and recipent cannot be empty
"""


def test_package_init_and_getters():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    assert package.get_dimensions() == (10, 25, 45)
    assert package.get_weight() == 120
    assert package.get_sender() == "heSends"
    assert package.get_recipent() == "heReceives"


def test_package_init_empty_sender_recipent():
    with pytest.raises(ValueError):
        package = Package("", "heReceives", 10, 25, 45, 120)
    with pytest.raises(ValueError):
        package = Package("heSends", "", 10, 25, 45, 120)
    with pytest.raises(ValueError):
        package = Package("", "", 10, 25, 45, 120)


def test_package_init_negative_or_zero_values():
    with pytest.raises(ValueError):
        package = Package("heSends", "heReceives", -10, 25, 45, 120)
    with pytest.raises(ValueError):
        package = Package("heSends", "heReceives", 10, -25, 45, 120)
    with pytest.raises(ValueError):
        package = Package("heSends", "heReceives", 10, 25, -45, 120)
    with pytest.raises(ValueError):
        package = Package("heSends", "heReceives", 10, 25, 45, -120)
    with pytest.raises(ValueError):
        package = Package("heSends", "heReceives", 0, 25, 45, 120)
    with pytest.raises(ValueError):
        package = Package("heSends", "heReceives", 10, 0, 45, 120)
    with pytest.raises(ValueError):
        package = Package("heSends", "heReceives", 10, 25, -45, 0)


def test_package_set_sender():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    package.set_sender("newSender")
    assert package.get_sender() == "newSender"


def test_package_set_sender_empty_sender():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    with pytest.raises(ValueError):
        package.set_sender("")


def test_package_set_recipent():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    package.set_recipent("newRecipent")
    assert package.get_recipent() == "newRecipent"


def test_package_set_recipent_empty_recipent():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    with pytest.raises(ValueError):
        package.set_recipent("")


def test_package_set_dimensions():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    package.set_dimensions((25, 67, 21))
    assert package.get_dimensions() == (25, 67, 21)


def test_package_set_dimensions_invalid_tuple():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    with pytest.raises(ValueError):
        package.set_dimensions((25, 67))
    with pytest.raises(ValueError):
        package.set_dimensions((25, 67, 21, 43))
    with pytest.raises(ValueError):
        package.set_dimensions(())


def test_package_set_dimensions_negative_or_zero():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)

    with pytest.raises(ValueError):
        package.set_dimensions((25, 0, 21))
    with pytest.raises(ValueError):
        package.set_dimensions((0, 5, 21))
    with pytest.raises(ValueError):
        package.set_dimensions((25, 0, -21))
    with pytest.raises(ValueError):
        package.set_dimensions((-25, 45, 21))


def test_package_set_weight():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    package.set_weight(35)
    assert package.get_weight() == 35


def test_package_set_weight_negative_or_zero():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    with pytest.raises(ValueError):
        package.set_weight(0)
    with pytest.raises(ValueError):
        package.set_weight(-19)


def test_package_min_dimension():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    assert package.min_dimension() == 10

    package = Package("heSends", "heReceives", 10, 6, 45, 120)
    assert package.min_dimension() == 6

    package = Package("heSends", "heReceives", 10, 5, 2, 120)
    assert package.min_dimension() == 2


def test_package_max_dimension():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    assert package.max_dimension() == 45

    package = Package("heSends", "heReceives", 10, 22856, 45, 120)
    assert package.max_dimension() == 22856

    package = Package("heSends", "heReceives", 1330, 5, 2, 120)
    assert package.max_dimension() == 1330


def test_package__str__():
    package = Package("heSends", "heReceives", 10, 25, 45, 120)
    assert (
        str(package)
        == "this packet is send by heSends to heReceives, with dimensions ranging from 10cm to 45cm and weighing 120kg"
    )


def test_package__str__float():
    package = Package("heSends", "heReceives", 10.56, 25, 45, 120)
    assert (
        str(package)
        == "this packet is send by heSends to heReceives, with dimensions ranging from 10.56cm to 45.00cm and weighing 120kg"
    )
