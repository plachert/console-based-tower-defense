from towers.towers import Tower
from waves.monsters import Monster
from typing import List

class Field:

    marker=None

    def __init__(self, x, y):
        self.objects = []
        self.x = x
        self.y = y

    def __str__(self):
        if self.objects:
            return self.objects[0].marker
        else:
            return self.marker

    def add_object(self, object):
        raise NotImplementedError

    def remove_object(self, object):
        self.objects.remove(object)

    def taxi_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


class WallField(Field):
    marker = '#'

    def attack(self, monsters: List[Monster]):
        for monster in monsters:
            self.objects[0].attack(monster)

    def add_object(self, object: Tower):
        if self.objects:
            raise ValueError("Field occupied")
        self.objects.append(object)


class PathField(Field):
    marker = '.'

    def __init__(self, x, y):
        super().__init__(x, y)
        self.observers = []

    def add_observer(self, observer: WallField):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.attack(self.objects)

    def add_object(self, object: Monster):
        self.objects.append(object)