from typing import Tuple

class Monster:
    marker="M"
    speed=1
    hp=100
    is_alive=True


class SlowMonster(Monster):
    marker = "S"
    hp = 10000
    update_move = 3 # speed

class FastMonster(Monster):
    marker = "F"
    hp = 100
    update_move = 1