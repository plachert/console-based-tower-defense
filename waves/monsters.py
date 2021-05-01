
class PassedTheGateError(Exception):
    pass

class Monster:
    marker="m"
    move_step=1
    hp=20
    points=10
    is_alive=True

    def __init__(self):
        self.ready = True
        self.path = None
        self.path_order = None
        self.position = None
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

class Speedy(Monster):
    marker="s"
    hp=20
    gold=100
    points=5
    move_step = 1 # speed

class Tank(Monster):
    marker = "t"
    hp = 200
    gold = 200
    move_step = 10
