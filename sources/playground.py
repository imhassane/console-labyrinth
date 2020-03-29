class Playground:

    def __init__(self, _map, player):
        self.map = _map
        self.player = player
        self.player_last_position = (0, 0)
        self.out_reached = False

    def move_player(self, direction, steps=1):

        if direction == 'l':
            if self.player.x > 0 and self.map.map[self.player.y][self.player.x - 1] == ' ':
                self.player_last_position = self.player.get_position()
                self.player.x -= steps

        elif direction == 'r':
            if self.player.x < self.map.width and self.map.map[self.player.y][self.player.x + 1] == ' ':
                self.player_last_position = self.player.get_position()
                self.player.x += steps

        elif direction == 't':
            if self.player.y > 0 and self.map.map[self.player.y - 1][self.player.x] == ' ':
                self.player_last_position = self.player.get_position()
                self.player.y -= steps

        elif direction == 'b':
            if self.player.y < self.map.height and self.map.map[self.player.y + 1][self.player.x] == ' ':
                self.player_last_position = self.player.get_position()
                self.player.y += steps

        else:
            pass

    def update(self):

        x, y = self.player_last_position
        self.map.set_element(' ', x, y)

        x, y = self.player.get_position()

        if self.map.map[y][x] == 'o':
            self.out_reached = True

        self.map.set_element(self.player.character, x, y)

    def __str__(self):
        pg_str = ""
        for row in self.map.map:
            pg_str += "".join(row) + "\n"

        return pg_str


if __name__ == "__main__":
    from sources.player import Player
    from sources.map import Map

    player = Player(0, 0)

    file_content = "pemem\nmemmm\nmeemm\nmmemm\noeemm"
    lab = Map(file_content)
    lab.build_map()

    pg = Playground(lab, player)

    pg.move_player('r')
    pg.update()

    pg.move_player('l')
    pg.update()

    pg.move_player('r')
    pg.update()

    pg.move_player('b')
    pg.update()

    pg.move_player('b')
    pg.update()

    print(pg)
