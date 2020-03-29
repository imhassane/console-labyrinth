def main():
    level_manager = LevelManager()
    level_manager.get_content()

    player = Player(0, 0)

    carte = Map(level_manager.content)
    carte.build_map()

    if carte.is_valid:
        pg = Playground(carte, player)

        print("###       WELCOME TO THE GRAND LABYRINTH GAME      ###")
        print("###       MAKE SURE YOU DON'T LOSE YOURSELF THERE  ###")

        play = True

        while play:
            # Printing the map.
            print(pg)

            # user's input
            try:
                direction = input("Left: l - Right: r - Top: t - Bottom: b: >> ")
                assert direction in "lrtb"

                pg.move_player(direction)
                pg.update()

                if pg.out_reached is True:
                    # If the user reaches the door
                    # we get the next level if he wants to continue.
                    cont = input("You have won!!!, do you want to play the next level ?: o: Yes >> ").lower()
                    if cont == "o":

                        level_manager.get_next_level()
                        level_manager.get_content()

                        carte = Map(level_manager.content)
                        player = Player(0, 0)
                        pg = Playground(carte, player)

                    else:
                        play = False

            except AssertionError:
                pass

    else:
        print("The map is not valid")


if __name__ == "__main__":
    from sources import Playground, Player, Map, LevelManager

    main()
