from collections import OrderedDict
from typing import Tuple

from fields.field import PathField, WallField
from towers.tower import Tower
from waves.monsters import Monster


class Map:
    ROWS=9
    COLUMNS=41

    def __init__(self):
        self.path = OrderedDict()
        self.wall = OrderedDict()
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                self.wall[(row, col)] = WallField(row, col)
        self._create_path()
        self.path_order = list(self.path.keys())
        self.monsters = []

    def build_tower(self, tower: Tower, position: Tuple[int, int]):
        self.wall[position].add_object(tower)
        for pos in self.path_order:
            field = self.path[pos]
            if field.taxi_distance(self.wall[position]) <= tower.range_:
                field.add_observer(self.wall[position])

    def add_monster(self, monster: Monster):
        monster.put_on_path(self.path)
        self.monsters.append(monster)

    def remove_monster(self, monster: Monster):
        self.monsters.remove(monster)

    def _create_path(self):
        def build_path_block(row, col):
            self.path[(row, col)] = PathField(row, col)
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

    def get_rows(self):
        map_rows = []
        for row in range(self.ROWS):
            row_str = []
            for col in range(self.COLUMNS):
                if (row, col) in self.wall.keys():
                    val = self.wall[(row, col)]
                else:
                    val = self.path[(row, col)]
                row_str.append(val.__str__())
            map_rows.append(row_str)
        return map_rows

    def print_with_monits(self, monits):
        rows = self.get_rows()
        for i, monit in enumerate(monits):
            rows[i].append(f"   {monit}")

        for row in rows:
            print("".join(row))
