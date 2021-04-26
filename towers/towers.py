from waves.monsters import Monster

class Tower:
    marker="T"
    price=30
    force=10

    def attack(self, monster: Monster):
        monster.hp -= self.force
        if monster.hp <=0:
            monster.is_alive = False

class CannonTower(Tower):
    marker="C"
    price=30

tower_dict = {"C": CannonTower}