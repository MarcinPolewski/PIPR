from classes import Game, Player, Enemy


# jeśli wywołujemy program bezpośrednio,
# nie przez import czy testy
def main():
    player = Player("zenek", 20)
    enemies = [Enemy("ANMA", 500), Enemy("Dwarf", 20)]
    game = Game(player, enemies)
    game.play(5)


if __name__ == "__main__":
    main()
