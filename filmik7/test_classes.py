from classes import Player, Enemy, Hydra, DragonHydra, Game
from classes import (
    NegativeLivesError,
    NameError,
    NonNaturalLibsNumberError,
    NegativePowerError,
)
import pytest


def test_create_player():
    player = Player("Jurek Ogórek", power=10)
    assert player.name() == "Jurek Ogórek"
    assert player.power == 10


def test_create_player_negativ_lives():
    with pytest.raises(ValueError):
        player = Player("Jurek Ogórek", -12)


def test_compare_players_different():
    """we test if instances are the same player"""
    jurek = Player("Jurek Ogórek", 10)
    karolina = Player("Karolina Malina", 25)

    assert not (jurek == karolina)


def test_compare_players_after_assignment():
    """we test if instances are the same player"""
    jurek = Player("Jurek Ogórek", 10)
    inny_jurek = Player("Jurek Ogórek", 20)

    inny_jurek = jurek
    # przypisujemy  referencje z obiektu po prawej do klamki po lewej
    assert inny_jurek == jurek


def test_create_player_with_lives():
    player = Player("Jurek Ogórek", 4)
    assert player.power == 4


def test_introduce():
    player = Player("Jurek Ogórek", 3)
    assert player.info() == "My name is Jurek Ogórek. I have 3 points of power!"

    player = Player("Jurek Ogórek", 1)
    assert player.info() == "My name is Jurek Ogórek. I have 1 point of power!"


def test_introduce_as_str():
    player = Player("Jurek Ogórek", 3)
    assert str(player) == player.info()

    player = Player("Jurek Ogórek", 1)
    assert str(player) == player.info()


def test_set_name():
    player = Player("Jurek Ogórek", 10)
    assert player.name() == "Jurek Ogórek"
    player.set_name("karolina malina")
    assert player.name() == "Karolina Malina"


def test_set_name_empty():
    player = Player("Jurek Ogórek", power=10)
    assert player.name() == "Jurek Ogórek"
    with pytest.raises(NameError):
        player.set_name("")


def test_get_player_lives_typical():
    player = Player("Jurek Ogórek", power=10)
    assert player.power == 10

    player = Player("Jurek Ogórek", power=36)
    assert player.power == 36


def test_set_lives_typical():
    player = Player("Jurek Ogórek", power=1)
    assert player.power == 1
    player.set_power(74)
    assert player.power == 74


def test_set_lives_convertable():
    player = Player("Jurek Ogórek", power="30")
    assert player.power == 30
    player.set_power("64")
    assert player.power == 64


def test_set_lives_not_convertable():
    player = Player("Jurek Ogórek", power=10)
    with pytest.raises(ValueError):
        player.set_power("dupa dupa blada dupa")


def test_set_lives_empty():
    player = Player("Jurek Ogórek", power=10)
    with pytest.raises(ValueError):
        player.set_power("")


def test_set_lives_negative():
    player = Player("Jurek Ogórek", power=20)
    with pytest.raises(NegativePowerError):
        player.set_power("-5")


def test_Player_attack(monkeypatch):
    player = Player("Jurek Ogórek", power=20)
    enemy1 = Hydra("nsadf", 1, 100)
    enemy2 = Hydra("1234", 2, 200)
    enemies = [enemy1, enemy2]

    def returnEnemy1(a):
        return enemy1

    def returnPlayerPower(a, b):
        return player.power

    monkeypatch.setattr("classes.randint", returnPlayerPower)
    monkeypatch.setattr("classes.choice", returnEnemy1)

    player.attack(enemies)
    assert player.power == 19
    assert enemy1.health == 80
    assert enemy2.health == 200


def test_enemy_init():
    enemy = Enemy("Łysy", 100)
    assert enemy.get_name() == "Łysy"
    assert enemy.get_health() == 100

    enemy = Enemy("łysy", 100)
    assert enemy.get_name() == "Łysy"
    assert enemy.get_health() == 100

    enemy = Enemy("łYSy", 100)
    assert enemy.get_name() == "Łysy"
    assert enemy.get_health() == 100


def test_enemy_init_negativ_health():
    with pytest.raises(NegativeLivesError):
        enemy = Enemy("łYSy", -100)


def test_enemy_empty_argument():
    with pytest.raises(NameError):
        enemy = Enemy("", 100)


def test_enemy_info():
    enemy = Enemy("Łysy", 100)
    assert enemy.info() == "This is Łysy, health: 100, is alive."


def test_enemy_take_damage():
    enemy = Enemy("Łysy", 100)
    enemy.take_damage(5)
    assert enemy.get_health() == 95


def test_enemy_take_damage_return():
    enemy = Enemy("Łysy", 100)
    assert enemy.take_damage(5)


def test_enemy_take_damage_zero_end_value():
    enemy = Enemy("Łysy", 5)
    enemy.take_damage(5)
    assert enemy.get_health() == 0


def test_enemy_take_damage_negative_end_Value():
    enemy = Enemy("Łysy", 5)
    enemy.take_damage(10)
    assert enemy.get_health() == 0


def test_enemy_take_damage_negative():
    with pytest.raises(NegativeLivesError):
        enemy = Enemy("Łysy", 5)
        enemy.take_damage(-10)


def test_enemy_is_alive():
    enemy = Enemy("Łysy", 5)
    assert enemy.is_alive()
    enemy.take_damage(5)
    assert not (enemy.is_alive())


def test_enemy_set_health():
    enemy = Enemy("Łysy", 5)
    assert enemy.get_health() == 5
    enemy.set_health(10)
    assert enemy.get_health() == 10


def test_enemy_set_health_negative():
    enemy = Enemy("Łysy", 5)
    with pytest.raises(ValueError):
        enemy.set_health(-1)


def test_hydra_init():
    hydra = Hydra("Jórek the Hydra", health=20, heads=3)
    hydra = Hydra("Jórek the Hydra", heads=3, health=45)

    hydra = Hydra("dupa dupa dupa", health=10)
    assert hydra.heads == 1


def test_hydra_non_natural_heads():
    with pytest.raises(NonNaturalLibsNumberError):
        hydra = Hydra("Jórek the Hydra", health=20, heads=0)
    with pytest.raises(NonNaturalLibsNumberError):
        hydra = Hydra("Jórek the Hydra", health=20, heads=-3)


def test_heads():
    hydra = Hydra("Jórek the Hydra", heads=3, health=45)
    assert hydra.heads == 3

    hydra = Hydra("Jórek the Hydra", health=5, heads=1234)
    assert hydra.heads == 1234


def test_hydra_description():
    hydra = Hydra("Jórek the Hydra", heads=3, health=45)
    assert (
        str(hydra) == "This is Jórek The Hydra, health: 45, is alive. It has 3 heads."
    )


def test_hydra_MAX_HEALTH():
    hydra = Hydra("Jórek the Hydra", heads=3, health=45)
    assert hydra.MAX_HEALTH == 45
    hydra.take_damage(10)
    assert hydra.MAX_HEALTH == 45
    assert hydra.health == 35


def test_hydra_regenerate():
    hydra = Hydra("Lysol", heads=2, health=500)
    hydra.take_damage(100)
    assert hydra.health == 400
    hydra.regenerate(50)
    assert hydra.health == 450


def test_hydra_regenerate_above_max():
    hydra = Hydra("Lysol", heads=2, health=500)
    hydra.take_damage(100)
    assert hydra.health == 400
    hydra.regenerate(10000)
    assert hydra.health == 500


def test_hydra_regenerate_negative():
    hydra = Hydra("Lysol", heads=2, health=500)
    with pytest.raises(NegativeLivesError):
        hydra.regenerate(-10)


def test_hydra_regenerate_non_convertable():
    hydra = Hydra("Lysol", heads=2, health=500)
    with pytest.raises(ValueError):
        hydra.regenerate("bajojoajojaojaosdjf")


def test_hydra_set_health():
    hydra = Hydra("Lysol", heads=2, health=500)
    assert hydra.health == 500

    hydra.set_health(50)
    assert hydra.health == 50

    hydra.set_health(1000)
    assert hydra.health == 500


# to jest zły test????
def test_DragonHydra_take_damage():
    did_avoid = False
    took_damage = False

    dh = DragonHydra(name="Franek", heads=1, health=1000)
    for i in range(100):
        dh.take_damage(1)

    if dh.health != 900:
        did_avoid = True
    if dh.health != 1000:
        took_damage = True

    assert did_avoid
    assert took_damage


def test_DragonHydra_take_damage_return_avoided(monkeypatch):
    dh = DragonHydra("lasdkjf", heads=2, health=50)

    def returnTrue(a, b):
        return True

    monkeypatch.setattr("classes.randint", returnTrue)

    assert dh.take_damage(50) is False


def test_DragonHydra_take_damage_didnt_avoid(monkeypatch):
    def returnFalse(t, f):
        return False

    monkeypatch.setattr("classes.randint", returnFalse)

    enemy = DragonHydra("Łysy", heads=1, health=1000)
    enemy.take_damage(5)
    assert enemy.get_health() == 995


def test_DragonHydra_take_damage_avoided(monkeypatch):
    def returnTrue(a1, a2):
        return True

    monkeypatch.setattr("classes.randint", returnTrue)

    enemy = DragonHydra("Łysy", heads=1, health=1000)
    enemy.take_damage(5)
    assert enemy.get_health() == 1000


def test_Game_init():
    # jezeli podamy wrogow czy sa w enemies,
    player = Player("jórek the Player")
    enemy1 = Hydra("Hydra1", 1, 100)
    enemy2 = Hydra("Hydra2", 2, 200)
    enemies = [enemy1, enemy2]

    game = Game(player, enemies=enemies)

    assert game.player == player
    assert game.enemies == enemies


def test_Game_init_empty_enemies():
    player = Player("jórek the Player")
    game = Game(player)

    assert game.player == player
    assert game.enemies == []
