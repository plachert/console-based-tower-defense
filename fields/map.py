from collections import OrderedDict
from towers.towers import Tower
from waves.monsters import SlowMonster, FastMonster, Monster
from typing import Tuple
from time import sleep
import reprint
from fields.field import PathField, WallField

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

    def populate_field(self, monster: Monster, position: Tuple[int, int]):
        self.path[position].add_object(monster)

    def depopulate_field(self, monster: Monster, position: Tuple[int, int]):
        self.path[position].remove_object(monster)

    def add_monster(self, monster: Monster):
        self.path[self.path_order[0]].add_object(monster)

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

    def __str__(self):
        map_string = []
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                if (row, col) in self.wall.keys():
                    val = self.wall[(row, col)]
                else:
                    val = self.path[(row, col)]
                map_string.append(val.__str__())
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
            objects = self.map.path[pos].objects
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
