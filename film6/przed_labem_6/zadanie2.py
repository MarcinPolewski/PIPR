class Package:
    """
    :param x: dimension x of a packet in cm
    :type x: float

    :param y: dimension y of a packet in cm
    :type y: float

    :param z: dimension z of a packet in cm
    :type z: float

    :param weight: weight of packet in kg
    :type weight: float

    :param sender: identificatory name of a person, who sent a packet
    :type sender: str

    :param recipent: identificatory name of a  person, who will receive a packet
    :type recipent: str



    """

    def __init__(
        self, sender: str, recipent: str, x: float, y: float, z: float, weight: float
    ):
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError("dimensions cannot be nonpositive")
        if weight <= 0:
            raise ValueError("weight cannot be nonpositive")

        if (not recipent) or (not sender):
            raise ValueError("recipent and sender cannot be empty")

        self._sender = sender
        self._recipent = recipent
        self._x = x
        self._y = y
        self._z = z
        self._weight = weight

    def get_dimensions(self) -> tuple:
        """return tuple of 3 floats descriping dimensions of packet"""
        return self._x, self._y, self._z

    def get_weight(self) -> float:
        """return weight of packet"""
        return self._weight

    def get_sender(self) -> str:
        """returns sender of a packet"""
        return self._sender

    def get_recipent(self):
        """returns a recipent of a packet"""
        return self._recipent

    def set_dimensions(self, new_dimensions: tuple):
        """sets packet's dimensions to values provided in tuple (x,y,z) respectively"""
        if len(new_dimensions) != 3:
            raise ValueError("tuple of new dimensions must have 3 elements")
        new_x, new_y, new_z = new_dimensions
        if new_x <= 0 or new_y <= 0 or new_z <= 0:
            raise ValueError("dimensions must me positive numbers")

        self._x = new_x
        self._y = new_y
        self._z = new_z

    def set_weight(self, new_weight):
        """sets weight of a packet to provied value"""
        if new_weight <= 0:
            raise ValueError("weight cannot be nonpositive")

        self._weight = new_weight

    def set_sender(self, new_sender):
        """sets sender of packet to provided str"""
        if not new_sender:
            raise ValueError("sender field cannot be empty")
        self._sender = new_sender

    def set_recipent(self, new_recipent):
        """sets recipent of a packet to provied str"""
        if not new_recipent:
            raise ValueError("recipent field cannnot be set to emppty")
        self._recipent = new_recipent

    def min_dimension(self) -> float:
        """returns minimal dimension of a packet"""
        return min(self._x, self._y, self._z)

    def max_dimension(self) -> float:
        """returns maximal dimension of a packet"""
        return max(self._x, self._y, self._z)

    def __str__(self):
        if self._x.is_integer() and self._y.is_integer() and self._z.is_integer():
            return f"this packet is send by {self._sender} to {self._recipent}, with dimensions ranging from {self.min_dimension()}cm to {self.max_dimension()}cm and weighing {self._weight}kg"
        return f"this packet is send by {self._sender} to {self._recipent}, with dimensions ranging from {self.min_dimension():.2f}cm to {self.max_dimension():.2f}cm and weighing {self._weight}kg"
