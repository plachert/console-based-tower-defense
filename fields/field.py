"""Implementation of map fields. Observer pattern (wallfield-pathfield)."""
from typing import List

from towers.tower import Tower
from waves.monsters import Monster


class Field:
    marker=None

    def __init__(self, pos_x, pos_y):
        self.objects = []
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        if self.objects:
            return self.objects[0].marker
        return self.marker

    def add_object(self, object_):
        raise NotImplementedError

    def remove_object(self, object_):
        self.objects.remove(object_)

    def taxi_distance(self, other):
        return abs(self.pos_x - other.pos_x) + abs(self.pos_y - other.pos_y)


class WallField(Field):
    marker='#'

    def attack(self, monsters: List[Monster]):
        for monster in monsters:
            self.objects[0].attack(monster)

    def add_object(self, object_: Tower):
        if self.objects:
            raise ValueError("Field occupied")
        self.objects.append(object_)


class PathField(Field):
    marker='.'

    def __init__(self, x, y):
        super().__init__(x, y)
        self.observers = []

    def add_observer(self, observer: WallField):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.attack(self.objects)

    def add_object(self, object_: Monster):
        self.objects.append(object_)
