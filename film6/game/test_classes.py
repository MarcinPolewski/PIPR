from classes import Player, Enemy
import pytest


def test_create_player():
    player = Player("Jurek Ogórek")
    assert player.name() == "Jurek Ogórek"


def test_create_player_negativ_lives():
    with pytest.raises(ValueError):
        player = Player("Jurek Ogórek", -12)


def test_compare_players_different():
    """we test if instances are the same player"""
    jurek = Player("Jurek Ogórek")
    karolina = Player("Karolina Malina")

    assert not (jurek == karolina)


def test_compare_players_same_name():
    """we test if instances are the same player"""
    jurek = Player("Jurek Ogórek")
    inny_jurek = Player("Jurek Ogórek")

    assert jurek == inny_jurek


def test_compare_players_after_assignment():
    """we test if instances are the same player"""
    jurek = Player("Jurek Ogórek")
    inny_jurek = Player("Jurek Ogórek")

    inny_jurek = jurek
    # przypisujemy  referencje z obiektu po prawej do klamki po lewej
    assert inny_jurek == jurek


def test_create_player_with_lives():
    player = Player("Jurek Ogórek", 4)
    assert player.get_lives() == 4


def test_introduce():
    player = Player("Jurek Ogórek", 3)
    assert player.info() == "My name is Jurek Ogórek. I have 3 lives left"

    player = Player("Jurek Ogórek", 1)
    assert player.info() == "My name is Jurek Ogórek. I have 1 life left"


def test_introduce_as_str():
    player = Player("Jurek Ogórek", 3)
    assert str(player) == player.info()

    player = Player("Jurek Ogórek", 1)
    assert str(player) == player.info()


def test_set_name():
    player = Player("Jurek Ogórek")
    assert player.name() == "Jurek Ogórek"
    player.set_name("karolina malina")
    assert player.name() == "Karolina Malina"


def test_set_name_empty():
    player = Player("Jurek Ogórek")
    assert player.name() == "Jurek Ogórek"
    with pytest.raises(ValueError):
        player.set_name("")


def test_get_player_lives_typical():
    player = Player("Jurek Ogórek")
    assert player.get_lives() == 1

    player = Player("Jurek Ogórek", 36)
    assert player.get_lives() == 36


def test_set_lives_typical():
    player = Player("Jurek Ogórek")
    assert player.get_lives() == 1
    player.set_lives(74)
    assert player.get_lives() == 74


def test_set_lives_convertable():
    player = Player("Jurek Ogórek")
    assert player.get_lives() == 1
    player.set_lives("64")
    assert player.get_lives() == 64


def test_set_lives_not_convertable():
    player = Player("Jurek Ogórek")
    with pytest.raises(ValueError):
        player.set_lives("dupa dupa blada dupa")


def test_set_lives_empty():
    player = Player("Jurek Ogórek")
    with pytest.raises(ValueError):
        player.set_lives("")


def test_set_lives_negative():
    player = Player("Jurek Ogórek")
    with pytest.raises(ValueError):
        player.set_lives("-5")


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
    with pytest.raises(ValueError):
        enemy = Enemy("łYSy", -100)


def test_enemy_empty_argument():
    with pytest.raises(ValueError):
        enemy = Enemy("", 100)


def test_enemy_info():
    enemy = Enemy("Łysy", 100)
    assert enemy.info() == "name: Łysy, health: 100, is alive"


def test_enemy_take_damage():
    enemy = Enemy("Łysy", 100)
    enemy.take_damage(5)
    assert enemy.get_health() == 95


def test_enemy_take_damage_zero_end_value():
    enemy = Enemy("Łysy", 5)
    enemy.take_damage(5)
    assert enemy.get_health() == 0


def test_enemy_take_damage_negative_end_Value():
    enemy = Enemy("Łysy", 5)
    enemy.take_damage(10)
    assert enemy.get_health() == 0


def test_enemy_take_damage_negative():
    with pytest.raises(ValueError):
        enemy = Enemy("Łysy", 5)
        enemy.take_damage(-10)


def test_enemy_is_alive():
    enemy = Enemy("Łysy", 5)
    assert enemy.is_alive()
    enemy.take_damage(5)
    assert not (enemy.is_alive())
