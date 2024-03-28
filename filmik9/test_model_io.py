from model_io import (
    read_from_csv,
    write_to_csv,
    read_from_json,
    write_to_json,
    InvalidLineError,
    InvalidPersonData,
    MalformedPersonDataError,
)
from model import Person, InvalidSexError
from database import PersonPermissionError, PersonPathNotFound, PersonPathIsADirectory
import pytest

from io import StringIO


def test_read_from_csv():
    #     data = """id,name,sex,birth_date
    # id1,name1,Female,1/1/2000
    # """
    data = "id,name,sex,birth_date\nid1,name1,Female,1/1/2000\n"

    file_handle = StringIO(data)
    people = read_from_csv(file_handle)
    assert len(people) == 1
    assert people[0].id == "id1"


def test_write_to_csv():
    person1 = Person("id1", "name1", "Female", "01/01/2001")
    person2 = Person("id2", "name2", "Female", "01/01/2002")

    people = [person1, person2]

    file_data = ""
    file_handle = StringIO(file_data)
    write_to_csv(file_handle, people)

    expected_result = (
        "id,name,sex,birth_date\n"
        + "id1,name1,Female,01/01/2001\n"
        + "id2,name2,Female,01/01/2002\n"
    )
    given_result = file_handle.getvalue()
    # print(given_result)
    # print(expected_result)
    assert given_result == expected_result


def test_read_missing_column_in_row():
    # name is missing in second line
    data = "id,name,sex,birth_date\nid1,Female,1/1/2000\n"
    file_handle = StringIO(data)

    with pytest.raises(MalformedPersonDataError):
        read_from_csv(file_handle)


def test_invalid_data():
    # invalid sex provided
    data = "id,name,sex,birth_date\nid1,name1,dupa,1/1/2000\n"
    file_handle = StringIO(data)

    with pytest.raises(InvalidPersonData):
        read_from_csv(file_handle)


def test_read_csv_write_json():
    with open("people.txt") as fp:
        people = read_from_csv(fp)
        with open("people.json", "w") as jsonfp:
            write_to_json(jsonfp, people)


def test_read_from_json():
    with open("people.json", "r") as fp:
        people = read_from_json(fp)
        assert len(people) == 1000


# def test_read_from_csv_manual():
#     with open("people.txt", "r") as file_handle:
#         read_from_csv(file_handle)


# dobrze by było podstawić do funkcji jakiś inny plik testowy,
# który znajdowałby się w wolderze tests


# def test_read_and_write():
#     people = []
#     with open("people.txt", "r") as file_handle:
#         people = read_from_csv(file_handle)
#     with open("output.txt", "w") as file_handle:
#         write_to_csv(file_handle, people)
