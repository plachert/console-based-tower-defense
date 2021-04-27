from typing import Tuple
# from fields.field import PathField

class PassedTheGateError(Exception):
    pass

class Monster:
    marker="M"
    move_step=1
    hp=20
    is_alive=True

    def __init__(self):
        self.ready = True
        self.time_count = 0

    def put_on_path(self, path):
        self.path = path
        self.path_order = list(self.path.keys())
        self.position = self.path_order[0]
        self.path[self.position].add_object(self)

    def get_index_on_path(self):
        return self.path_order.index(self.position)

    def berry_me(self):
        self.is_alive = False
        current = self.get_index_on_path()
        self.path[self.path_order[current]].remove_object(self)

    def move(self):
        if self.ready and self.is_alive:
            current = self.get_index_on_path()
            self.path[self.path_order[current]].remove_object(self)
            try:
                self.path[self.path_order[current + 1]].add_object(self)
                self.position = self.path_order[current + 1]
                self.path[self.path_order[current + 1]].notify_observers()
            except IndexError:
                raise PassedTheGateError
            self.ready = False

    def update(self):
        self.time_count += 1
        if self.time_count == self.move_step:
            self.ready = True
            self.time_count = 0

class SlowMonster(Monster):
    marker = "S"
    hp = 10000
    move_step = 3 # speed

class FastMonster(Monster):
    marker = "F"
    hp = 20
    move_step = 1