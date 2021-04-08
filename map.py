from collections import OrderedDict

class Map:
    ROWS=9
    COLUMNS=9

    def __init__(self):
        self.path = OrderedDict()
        self.wall = OrderedDict()
        for row_idx in range(self.ROWS):
            for col_idx in range(self.COLUMNS):
                self.wall[(row_idx, col_idx)] = None
        self._create_path()

    def _create_path(self):
        def build_path_block(row, col):
            self.path[(row, col)] = None
            self.wall.pop((row, col))
        row = 0
        col = self.COLUMNS - 2
        while row < self.ROWS - 1:
            build_path_block(row, col)
            row += 1
            for col in range(self.COLUMNS-2, 0, -1):
                build_path_block(row, col)
            for _ in range(2):
                row += 1
                build_path_block(row, col)
            for col in range(2, self.COLUMNS - 1):
                build_path_block(row, col)
            row += 1
        build_path_block(row, col)

    def __str__(self):
        for row in range(self.ROWS):
            row_string = []
            for col in range(self.COLUMNS):
                if (row, col) in self.wall.keys():
                    row_string.append("#")
                else:
                    row_string.append("P")
            print(row_string)
        return ""#str(self.path) + str(self.wall)


if __name__ == '__main__':
    map = Map()
    print(map)
    print(map.path)