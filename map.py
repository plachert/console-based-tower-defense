from collections import OrderedDict
from towers import Tower
from monsters import SlowMonster, FastMonster, Monster
from typing import Tuple
from time import sleep
import reprint

class Map:
    ROWS=9
    COLUMNS=21

    def __init__(self):
        self.path = OrderedDict()
        self.wall = OrderedDict()
        for row_idx in range(self.ROWS):
            for col_idx in range(self.COLUMNS):
                self.wall[(row_idx, col_idx)] = None
        self._create_path()
        self.path_order = list(self.path.keys())
        self.monsters = []

    def build_tower(self, tower: Tower, position: Tuple[int, int]):
        empty = self.get_empty_wall_blocks()
        if position in empty:
            self.wall[position] = tower

    def populate_field(self, monster: Monster, position: Tuple[int, int]):
        if self.path[position] is None:
            self.path[position] = [monster]
        else:
            self.path[position].append(monster)

    def depopulate_field(self, monster: Monster, position: Tuple[int, int]):
        return self.path[position].remove(monster)

    def add_monster(self, monster: Monster):
        self.populate_field(monster, position=self.path_order[0])

    def get_empty_wall_blocks(self):
        empty = [key for key, val in self.wall.items() if key is not None]
        return empty

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

    def get_rows(self):
        map_rows = []
        for row in range(self.ROWS):
            row_str = []
            for col in range(self.COLUMNS):
                if (row, col) in self.wall.keys():
                    val = self.wall[(row, col)]
                    if val is None:
                        row_str.append("#")
                    else:
                        tower_marker = val.marker
                        row_str.append(tower_marker)
                else:
                    val = self.path[(row, col)]
                    if val:
                        monster_marker = val[0].marker  # monsters can populate the same path block. Show one of them
                        row_str.append(monster_marker)
                    else:
                        row_str.append(" ")
            map_rows.append(row_str)
        return map_rows

    def __str__(self):
        map_string = []
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                if (row, col) in self.wall.keys():
                    val = self.wall[(row, col)]
                    if val is None:
                        map_string.append("#")
                    else:
                        tower_marker = val.marker
                        map_string.append(tower_marker)
                else:
                    val = self.path[(row, col)]
                    if val:
                        monster_marker = val[0].marker  # monsters can populate the same path block. Show one of them
                        map_string.append(monster_marker)
                    else:
                        map_string.append(" ")
            map_string.append("\n")
        return "".join(map_string)


class Simulation:

    def __init__(self, map):
        self.map = map
        self.timestep = 0

    def run(self):
        with reprint.output(output_type="dict", interval=0) as output_dict:
            while True:
                self.timestep += 1
                self.update()
                rows = self.map.get_rows()
                for i, row in enumerate(rows):
                    output_dict[i] = "{}".format("".join(row))
                sleep(0.1)


    def update(self):
        updated_monsters = []
        for i, pos in enumerate(self.map.path_order):
            objects = self.map.path[pos]
            if objects:
                for monster in objects:
                    if monster in updated_monsters:
                        continue
                    if not self.timestep % monster.update_move:
                        self.map.depopulate_field(monster, pos)
                        try:
                            next_field = self.map.path_order[i + 1]
                            self.map.populate_field(monster, next_field)
                        except IndexError:
                            print("death")
                        updated_monsters.append(monster)
            else:
                pass





if __name__ == '__main__':
    map = Map()
    tower = Tower()
    monster1 = SlowMonster()
    monster2 = FastMonster()
    map.build_tower(tower, (0, 7))
    map.build_tower(tower, (2, 7))
    map.add_monster(monster1)
    map.add_monster(monster2)

    simulation = Simulation(map)
    simulation.run()
