from model import Person
import csv
import json


class InvalidLineError(Exception):
    def __init__(self, line_number):
        super().__init__(f"invalid number of elements in line {line_number}")
        self._line_number = line_number


class InvalidPersonData(Exception):
    def __inti__(self, tokens):
        super().__inti__("Invalid Person arguments given")
        self._tokens = tokens

    @property
    def tokens(self):
        return self._tokens


class MalformedPersonDataError(Exception):
    pass


def read_from_csv(file_handle):
    people = []
    # domyślnie pierwszy wiersz zostanie potraktowany z
    reader = csv.DictReader(file_handle)
    try:
        for row in reader:
            id = row["id"]
            name = row["name"]
            sex = row["sex"]
            birth_date = row["birth_date"]
            if None in row.values():
                raise MalformedPersonDataError("Missing column in flie")
            try:
                person = Person(id, name, sex, birth_date)
            except Exception:
                raise InvalidPersonData((id, name, sex, birth_date))
            people.append(person)
    except csv.Error as e:
        raise MalformedPersonDataError(str(e))
    return people

    # # reads the first line, which we want to omit
    # file_handle.readline()
    # for line_idx, line in enumerate(file_handle):
    #     # getting rid of end of line char
    #     line = line.rstrip()
    #     tokens = line.split(",")
    #     try:
    #         id, name, sex, birth_date = tokens
    #     except Exception:
    #         raise InvalidLineError(line_idx)
    #     person = Person(id, name, sex, birth_date)
    #     people.append(person)
    # return people


def write_to_csv(file_handle, people):
    writer = csv.DictWriter(file_handle, ["id", "name", "sex", "birth_date"])
    writer.writeheader()
    try:
        for person in people:
            writer.writerow(
                {
                    "id": person.id,
                    "name": person.name,
                    "sex": person.sex,
                    "birth_date": person.birth_date,
                }
            )

    except csv.Error as e:
        raise MalformedPersonDataError(str(e))
    # file_handle.write("id,name,sex,birth_date\n")
    # for person in people:
    #     file_handle.write(
    #         str(person.id)
    #         + ","
    #         + person.name
    #         + ","
    #         + person.sex
    #         + ","
    #         + person.birth_date
    #         + "\n"
    #     )


def read_from_json(file_handle):
    people = []
    data = json.load(file_handle)
    for item in data:
        # elementami listy są słowniki
        try:
            id = item["id"]
            name = item["name"]
            sex = item["sex"]
            birth_date = item["birth_date"]
        except KeyError as e:
            raise MalformedPersonDataError("Missing key in file") from e
        try:
            person = Person(id, name, sex, birth_date)
        except Exception:
            raise InvalidPersonData((id, name, sex, birth_date)) from e
        people.append(person)

    return people


def write_to_json(file_handle, people):
    data = []
    for person in people:
        id = person.id
        name = person.name
        sex = person.sex
        birth_date = person.birth_date
        person_data = {"id": id, "name": name, "sex": sex, "birth_date": birth_date}
        data.append(person_data)
    json.dump(data, file_handle, indent=4)
