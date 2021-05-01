from waves.monsters import Monster

class Tower:
    marker="T"
    price=30
    force=10
    reload=10
    range_=2

    def __init__(self):
        self.ready = True
        self.time_count = 0

    def attack(self, monster: Monster):
        if self.ready:
            monster.hp -= self.force
            if monster.hp <= 0:
                monster.berry_me()
            self.ready = False

    def update(self):
        self.time_count += 1
        if self.time_count == self.reload:
            self.ready = True
            self.time_count = 0

class Archer(Tower):
    marker="A"
    force=10
    reload=2
    price=10
    range_=5

class Cannon(Tower):
    marker="C"
    force=50
    range_=2
    reload=15
    price=30

class Ranger(Tower):
    marker="R"
    range_=30
    force=20
    reload=20
    price=50


tower_dict = {"A": Archer,
              "C": Cannon,
              "R": Ranger}

def get_tower_info():
    pretty_dict = {}
    for letter, tower in tower_dict.items():
        pretty_dict[letter] = (tower.__name__, tower.price)
    return  pretty_dict