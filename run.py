import os
from time import sleep

import reprint

from fields.map import Map
from towers.tower import tower_dict
from waves.monsters import PassedTheGateError
from waves.wave import EasyWave, HeavyWave


class Game:
    def __init__(self):
        self.gold = 100
        self.lives = 30
        self.points = 0
        self.map = Map()
        self.waves = [EasyWave(), HeavyWave()]

    def build(self):
        def print_current():
            os.system("clear")
            self.map.print_with_monits([f"Available gold: {self.gold}",
                                        f"Lives: {self.lives}",
                                        f"Points: {self.points}"])
        print("Buliding phase")
        while True:
            print_current()
            if input("Want to buy? y/n ") == "n":
                break
            tower_selection = input("Enter tower name ")
            try:
                tower = tower_dict[tower_selection.upper()]()
            except KeyError:
                print("Wrong letter")
                continue
            price = tower.price
            if price > self.gold:
                print("Not enough gold")
                continue
            while True:
                row = int(input("Enter row number "))
                col = int(input("Enter col number "))
                try:
                    self.map.build_tower(tower, (row, col))
                    self.gold -= price
                    break
                except ValueError:
                    print("This field is unavailable")
                    continue
            print_current()
        os.system("clear")

    def fight(self):
        def get_current_status():
            monsters_hp = []
            for monster in self.map.monsters:
                monsters_hp.append(str(monster.hp))
            monsters_hp = " ".join(monsters_hp)
            return f" Monsters hp: {monsters_hp}"

        wave = self.waves.pop(0)
        with reprint.output(output_type="dict", interval=0) as output_dict:
            while True:
                self.update()
                wave.release(self.map)
                wave.update()
                rows = self.map.get_rows()
                rows[0] += get_current_status()
                rows[1] += f" Lives: {self.lives}"
                for i, row in enumerate(rows):
                    output_dict[i] = "{}".format("".join(row))
                sleep(0.1)
                if not self.map.monsters:
                    break
                if self.lives == 0:
                    break

    def update(self):
        for _, field in self.map.wall.items():
            if field.objects:
                tower = field.objects[0]
                tower.update()
        for monster in self.map.monsters:
            monster.update()
            if monster.is_alive:
                try:
                    monster.move()
                except PassedTheGateError:
                    # remove life
                    self.map.remove_monster(monster)
                    self.lives -= 1
            else:
                # add points for monster
                self.gold += monster.gold
                self.points += monster.points
                self.map.remove_monster(monster)

    def run(self):
        while self.waves:
            self.build()
            self.fight()


if __name__ == '__main__':
    game = Game()
    game.run()
