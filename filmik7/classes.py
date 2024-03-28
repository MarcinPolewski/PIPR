from random import randint, choice

class NegativePowerError(Exception):
    def __init__(self, power): 
        super().__init__("power count cannot be negative")
        self._lives = power

class NegativeLivesError(Exception):
    def __init__(self, lives): 
        super().__init__("Life count cannot be negative")
        self._lives = lives

class NameError(Exception):
    def __init__(self, name): 
        super().__init__("Invalid name provided")
        self._provided_name = name

class NonNaturalLibsNumberError(Exception): 
    def __init__(self, count): 
        super().__init__("Cannot set number of limbs(heads) to non natural != {1,2,3,..}")
        self._limbs_count = count

class Player:
    """
    Class Player. Contain attributes:
    :param name: player's name
    :type name: str

    :param lives: player's lives, defaults to 1
    :type lives: int

    :param
    """

    def __init__(self, name, power):
        self._name = name
        power = int(power)
        if power < 0:
            raise NegativePowerError(power)
        self._power = power

    def info(self):
        """
        Returns baisc description of the player
        """
        word_form = "point" if self._power == 1 else "points"
        return f"My name is {self._name}. I have {self._power} {word_form} of power!"

    def __str__(self):
        return self.info()

    def name(self):
        return self._name

    def set_name(self, new_name):
        if not new_name:
            raise NameError("new_name cannot be empty")
        self._name = str(new_name).title()

    @property
    def power(self):
        return self._power

    def set_power(self, new_power):
        if not (new_power):
            raise ValueError("new_lives_value is empty")

        new_power = int(new_power)
        if new_power < 0:
            raise NegativePowerError(new_power)
        self._power = new_power

    def attack(self, enemies):
        if self.power == 0 or not enemies:
            return (None, 0, False)
        damage = randint(0, self.power)
        enemy_to_attack = choice(enemies)
        attack_status = enemy_to_attack.take_damage(damage)
        self.set_power(max(0, self.power-1))
        return (enemy_to_attack, damage, attack_status)


class Enemy:
    """
    Contains attributes:
    :param _name: enemy's name
    :type: _name: str

    :param _health: contain healh value
    :type _health: int

    """

    def __init__(self, name, health=100):
        if not (name):
            raise NameError("name cannot be empty")
        health = int(health)
        if (health < 0):
            raise NegativeLivesError(health)
        self._name = name.title()
        self._health = int(health)

    def info(self):
        """ return string containg all information about enemy"""
        return f"This is {self._name}, health: {self._health}, {"is alive" if self.is_alive() else "dead"}."

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
            raise NegativeLivesError(hit_points)
        self._health = max(self._health - hit_points, 0)
        return True

    def set_health(self, new_health):
        new_health = int(new_health)
        if new_health < 0: 
            raise ValueError("Cannot set health to negative value")
        self._health = new_health

class Hydra(Enemy):
    def __init__(self, name, heads=1, health=100):
        super().__init__(name, health)
        if (heads < 1):
            raise NonNaturalLibsNumberError("Hydra cannot have non natural number of heads")
        self._heads = heads
        self._MAX_HEALTH = health

    @property
    def heads(self):
        return self._heads

    @property
    def health(self):
        return self._health

    @property
    def MAX_HEALTH(self):
        return self._MAX_HEALTH

    def __str__(self):
        description = super().info()
        description += f" It has {self.heads} heads."
        return description

    def regenerate(self, health_to_regenerate):
        health_to_regenerate = int(health_to_regenerate)
        if health_to_regenerate < 0:
            raise NegativeLivesError(health_to_regenerate)
        self._health = min(self._health + health_to_regenerate, self.MAX_HEALTH)

    def set_health(self, new_health):
        super().set_health(min(self.MAX_HEALTH, new_health))


class DragonHydra(Hydra):
    def take_damage(self, hit_points):
        is_avoided = bool(randint(0, 1))
        if is_avoided:
            return False
        super().take_damage(hit_points)
        return True

class Game():
    def __init__(self, player, enemies=None):
        self.player = player
        self.enemies = enemies if enemies else []               
        self._result = None
        #niezmiennik - dlatego prywatny

    def play(self, rounds):
        print(f"Starting game...{rounds} rounds will be played!")

        for round_counter in range(rounds):
            enemy_attacked, damage, attack_status = self.player.attack(self.enemies)
            if not enemy_attacked.is_alive():
                self.enemies.remove(enemy_attacked)
            print(f"Round {round_counter}:")
            if enemy_attacked is None:
                print("Nikogo nie zaatakowano")
            elif attack_status is True:
                print(f"Atak się powiódł, zaatakowano {enemy_attacked.get_name()} mocą {damage}")
            else:
                print("Atak się nie powiódł")

        self._result = bool(self.enemies)
        return self._result
