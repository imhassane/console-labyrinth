class Player:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.character = 'p'

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Player: %d, %d" % (self.x, self.y)


if __name__ == "__main__":
    p = Player(10, 10)
    print(p)
