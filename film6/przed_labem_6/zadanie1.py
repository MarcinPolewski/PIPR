class Planet:
    _moons_number = 0
    """
    :param x: position of planes on x axes
    :type x: int

    :param y: position of planes on y axes
    :type y: int

    :param z: position of planes on z axes
    :type z: int

    :param moons_number: how many moons does the planet have
    :type x: int

    :param name: planet's name
    :type name: str
    """

    def __init__(self, x, y, z, name=""):
        self._x = x
        self._y = y
        self._z = z
        self._name = name

    def get_moons_number(self) -> int:
        """ returns number of moons"""
        return self._moons_number

    def set_moons_number(self, new_moons_number):
        """ sets number of moons to given value """
        new_moons_number = int(new_moons_number)
        if new_moons_number < 0:
            raise ValueError("new_moons_number cannot be negative!")
        self._moons_number = new_moons_number

    def get_coordinates(self) -> tuple:
        """ return tuple of coordinated (x,y,z) respectively (coordinated are ints) """
        return self._x, self._y, self._z

    def set_coordinates(self, new_x, new_y, new_z):
        """ converts new coordinated to int, then assigns new values"""
        new_x = int(new_x)
        new_y = int(new_y)
        new_z = int(new_z)

        self._x = new_x
        self._y = new_y
        self._z = new_z

    def get_name(self) -> str:
        """ return planet name """
        return self._name

    def set_name(self, new_name):
        """ sets planet name to given string """
        self._name = str(new_name)

    def __str__(self) -> str:
        return f"My name is {self._name}, i am currently poistioned at {self.get_coordinates()} and I have {self._moons_number} {"mooon" if self._moons_number == 1 else "moons"}"
