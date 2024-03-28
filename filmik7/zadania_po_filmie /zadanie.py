class InvalidEmailError(Exception):
    def __init__(self, email):
        self._email = email
        super().__init__("Invalid email provided")


def emailIsValid(email) -> bool:
    if (not email) or email.count("@") != 1 or email[0] == "@" or email[-1] == "@":
        return False
    return True


class Employee:
    """
    atributes: name, email,
    """

    def __init__(self, name, email=None):
        if not name:
            raise ValueError
        if not email:
            email = f"{name.lower()}@company.com"
        elif not emailIsValid(email):
            raise InvalidEmailError(email)

        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    def set_name(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be empty")
        self._name = new_name

    @property
    def email(self):
        return self._email

    def set_email(self, new_email):
        if not new_email or (not emailIsValid(new_email)):
            raise InvalidEmailError(new_email)
        self._email = new_email


class FullTimeEmployee(Employee):
    """
    atribues: monthly salary
    """

    pass


class Manager(FullTimeEmployee):
    """
    atribues: reportingEmployees
    methods: add/remove workers from reportinEmployees
    """


class SoftwareEngineer(FullTimeEmployee):
    """
    atribues: programmingLanguage
    methods:
    """


class TechnicalWorker(Employee):
    """
    atribues: hourlyRate, workHoursMonthly
    methods: calculateSalary
    """
