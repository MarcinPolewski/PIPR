import pytest
from zadanie import (
    Employee,
    FullTimeEmployee,
    Manager,
    SoftwareEngineer,
    TechnicalWorker,
    emailIsValid,
)
from zadanie import (
    InvalidEmailError,
)


def test_emailIsValid():
    assert emailIsValid("aslkdf@alskdfj.com")


def test_emailIsValid_ats():
    assert not emailIsValid("aslkdfalskdfj.com")
    assert not emailIsValid("asl@kdfal@skdfj.com")
    assert not emailIsValid("@kdfal@skdfj.com")
    assert not emailIsValid("kdfal@skdfj.com@")


def test_emailIsValid_corner():
    assert not emailIsValid("")
    assert not emailIsValid(None)


def test_Employee():
    e1 = Employee(name="Jeff", email="jeff@company.com")
    assert e1.name == "Jeff"
    assert e1.email == "jeff@company.com"


def test_Employee_default_email():
    e1 = Employee(name="Jeff")
    assert e1.name == "Jeff"
    assert e1.email == "jeff@company.com"


def test_Employee_Excepctions():
    with pytest.raises(InvalidEmailError):
        e1 = Employee(name="Jeff", email="jeff@co@mp@any.com")
    with pytest.raises(ValueError):
        e1 = Employee(name="", email="jeff@co@mp@any.com")


def test_Employee_set_name():
    e1 = Employee(name="Jeff", email="jeff@company.com")
    e1.set_name("Scarlet")
    assert e1.name == "Scarlet"


def test_Employee_set_name_emplty():
    e1 = Employee(name="Jeff", email="jeff@company.com")
    with pytest.raises(ValueError):
        e1.set_name("")


def testEmployee_set_email():
    e1 = Employee(name="Scarlet", email="jeff@company.com")
    e1.set_email("Scarlet@company.com")
    assert e1.email == "Scarlet@company.com"


def test_Employee_set_email():
    e1 = Employee(name="Scarlet", email="jeff@company.com")
    with pytest.raises(InvalidEmailError):
        e1.set_email("")
    with pytest.raises(InvalidEmailError):
        e1.set_email("Scarletcompany")
    with pytest.raises(InvalidEmailError):
        e1.set_email("Scarlet@saf@company.com")
