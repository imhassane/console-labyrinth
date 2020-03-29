from os import path, walk


class LevelManager:

    def __init__(self, levels_dir="levels"):

        self.current_level = 0
        self.level_to_load = ""
        self.levels_dir = path.normpath(path.join(path.abspath("."), levels_dir))
        self.content = ""
        self.files = {}

        # Getting all the levels.
        self.__get_levels()

        # Getting the current level.
        self.__get_current_level()

    def __get_levels(self):

        for _, _, f in walk(self.levels_dir):
            f.sort()
            for i, file in enumerate(f):
                if '.cll' in file:
                    self.files[i + 1] = self.levels_dir + "/" + file

    def __get_current_level(self):

        with open(self.levels_dir + "/data.ld", "r") as file:
            content = file.read()

        if len(self.files.keys()) > 0:

            if content and len(content) > 0:
                try:
                    self.current_level = int(content)
                except ValueError:
                    self.current_level = 1
                finally:
                    self.level_to_load = self.files.get(self.current_level)

        else:
            self.level_to_load = ""

    def get_next_level(self):

        next_level = self.current_level + 1
        if next_level <= len(self.files.keys()):
            with open(self.levels_dir + "/data.ld", "w") as f:
                f.write(str(next_level))
            self.__get_current_level()

        else:
            self.reinitialize()

    def get_content(self):

        with open(self.level_to_load, "r") as f:
            self.content = f.read()

    def reinitialize(self):

        with open(self.levels_dir + "/data.ld", "w") as f:
            f.write("0")


if __name__ == "__main__":
    l = LevelManager("../levels")

    print(l.files)
    l.get_next_level()
    print(l.level_to_load)

