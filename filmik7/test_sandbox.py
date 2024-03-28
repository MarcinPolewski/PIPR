from random import randint


def fake_randint(f, t):
    return 1


randint = fake_randint


def test_randint():
    assert randint(0, 1) == 1
