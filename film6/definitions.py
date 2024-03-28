class Object:
    pass


class Person:
    def __init__(self, fname, sname, age_in=420):  # metoda specjalna, dlatego __ __
        self.first_name = fname
        self.last_name = sname
        self.age = age_in

    def introduce(me):
        """Object introduces itself"""
        return f"My name is {me.first_name} and my last name is {me.last_name}"
