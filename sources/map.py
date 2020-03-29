class Map:

    def __init__(self, file_content):
        # This is a string representing the actual map.
        self.file_content = file_content
        self.map = []
        self.width = 0
        self.height = file_content.count("\n") + 1
        self.is_valid = False

    def set_element(self, elem, x, y):
        self.map[y][x] = elem

    def build_map(self):

        line = []
        for c in self.file_content:
            if c == "\n":

                self.map.append(line)
                line = []
            else:
                if c == 'e':
                    c = ' '
                line.append(c)

        try:
            # We assert that all the lines has the same size
            rows = len(self.map)
            columns = 0

            if rows > 0:
                columns = len(self.map[0])

            for row in self.map:
                assert len(row) == columns

            self.width = columns
            self.is_valid = True

        except AssertionError:
            self.is_valid = False

    def __str__(self):

        return "Informations\n\tValid: %s\n\tHeight: %d\n\tWidth: %d\n\tMap: %s" % (self.is_valid, self.height, self.width, self.map)


if __name__ == "__main__":
    # Correct
    file_content = "iemmm\nmemmm\nmeemm\nmmemm\noeemm"

    map = Map(file_content)
    map.build_map()
    print(map)

    print("----------------------------------------")
    # Not correct
    file_content = "iem\nmemmm\nmeemm\nmmemm\noeemm"

    map = Map(file_content)
    map.build_map()
    print(map)
