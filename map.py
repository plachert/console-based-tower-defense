
class Map:
    ROWS=5
    COLUMNS=5

    def __init__(self):
        self.path = []
        self.wall = []
        for row_idx in range(self.ROWS):
            for col_idx in range(self.COLUMNS):
                self.wall.append((row_idx, col_idx, "#"))
        self._create_path()

    def _create_path(self):
        row = 0
        col = self.COLUMNS - 2
        while row < self.ROWS - 1:
            self.path.append((row, col, ""))
            row += 1
            for _ in range(self.COLUMNS - 3):
                self.path.append((row, col, ""))
                col -= 1
            for _ in range(2):
                self.path.append((row, col, ""))
                row += 1
            for _ in range(self.COLUMNS - 3):
                self.path.append((row, col, ""))
                col += 1
            row += 1
            self.path.append((row, col, ""))

    def __str__(self):
        return str(self.path)


if __name__ == '__main__':
    map = Map()
    print(map)