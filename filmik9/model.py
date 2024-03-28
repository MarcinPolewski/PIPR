class InvalidNameError(Exception):
    def __init__(self, name):
        super().__init__(
            f"name must not be empty and must not contain numbers, {name} provided"
        )
        self._name = name

    @property
    def name(self):
        return self._name


class InvalidSexError(Exception):
    def __init__(self, sex):
        super().__init__(f"sex must be str either Male or Female, {sex} provided")
        self._sex = sex

    @property
    def sex(self):
        return self._sex


class Person:
    def __init__(self, id, name, sex, birth_date):
        if not name:
            raise InvalidNameError(name)
        if sex not in ["Male", "Female"]:
            raise InvalidSexError(sex)

        self._id = id
        self._name = name
        self._sex = sex
        self._birth_date = birth_date

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def sex(self):
        return self._sex

    @property
    def birth_date(self):
        return self._birth_date

    def __str__(self):
        return self._name
