from waves.monsters import Monster

class Tower:
    marker="T"
    price=30
    force=10
    reload=10

    def __init__(self):
        self.ready = True
        self.time_count = 0

    def attack(self, monster: Monster):
        if self.ready:
            print("attack")
            monster.hp -= self.force
            if monster.hp <=0:
                monster.is_alive = False
            self.ready = False

    def update(self):
        self.time_count += 1
        if self.time_count == self.reload:
            self.ready = True
            self.time_count = 0

class CannonTower(Tower):
    marker="C"
    price=30

tower_dict = {"C": CannonTower}