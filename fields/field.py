from towers.towers import Tower
from waves.monsters import Monster

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

    def add_object(self, object: Tower):
        if self.objects:
            raise ValueError("Field occupied")
        self.objects.append(object)


class PathField(Field):
    marker = '.'

    def add_object(self, object: Monster):
        self.objects.append(object)