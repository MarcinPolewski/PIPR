class Player:
    """
    Class Player. Contain attributes:
    :param name: player's name
    :type name: str

    :param lives: player's lives, defaults to 1
    :type lives: int

    :param
    """

    def __init__(self, name, lives=1):
        self._name = name
        lives = int(lives)
        if lives < 0:
            raise ValueError("Lives count cannot be negative")
        self._lives = lives

    def info(self):
        """
        Returns baisc description of the player
        """
        word_form = "life" if self._lives == 1 else "lives"
        return f"My name is {self._name}. I have {self._lives} {word_form} left"

    def __str__(self):
        return self.info()

    def name(self):
        return self._name

    def set_name(self, new_name):
        if not new_name:
            raise ValueError("new_name cannot be empty")
        self._name = str(new_name).title()

    def get_lives(self):
        return self._lives

    def set_lives(self, new_lives_value):
        if not (new_lives_value):
            raise ValueError("new_lives_value is empty")

        new_lives_value = int(new_lives_value)
        if new_lives_value < 0:
            raise ValueError("value of lives cannot be negative!")
        self._lives = new_lives_value


class Enemy:
    """
    Contains attributes:
    :param _name: enemy's name
    :type: _name: str

    :param _health: contain healh value
    :type _health: int

    """

    def __init__(self, name, health=100):
        if not(name):
            raise ValueError("name cannot be empty") 
        health = int(health)
        if (health < 0):
            raise ValueError("health cannot be <0")
        self._name = name.title()
        self._health = int(health)


    def info(self):
        """ return string containg all information about enemy"""
        return f"name: {self._name}, health: {self._health}, {"is alive" if self.is_alive() else "dead"}"

    def get_name(self):
        """return name of enemy"""
        return self._name

    def get_health(self):
        """ returns health of enemy """
        return self._health

    def is_alive(self):
        """if enemy is alive return true"""
        return self._health > 0 

    def take_damage(self, hit_points):
        """ decreases enemy's health points by given value """
        hit_points = int(hit_points)
        if hit_points < 0: 
            raise ValueError("Take_damage() cannot take negative value")
        self._health = max(self._health - hit_points, 0)



