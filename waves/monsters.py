from typing import Tuple

class Monster:
    marker="M"
    speed=1

class SlowMonster(Monster):
    marker = "S"
    update_move = 3 # speed

class FastMonster(Monster):
    marker = "F"
    update_move = 1