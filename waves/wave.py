from waves.monsters import Speedy, Tank

class Wave:

    def __init__(self):
        self.lobby = []
        self.ready = True
        self.time_count = 0
        self.fill()

    def fill(self):
        raise NotImplementedError

    def release(self, map):
        if self.lobby and self.ready:
            monster = self.lobby.pop()
            map.add_monster(monster)
            self.ready = False

    def get_lobby_time(self):
        if self.lobby:
            monster = self.lobby[-1]
            return monster.move_step
        else:
            return 0

    def update(self):
        self.time_count += 1
        if self.time_count == self.get_lobby_time():
            self.ready = True
            self.time_count = 0

class EasyWave(Wave):

    def fill(self):
        for _ in range(20):
            self.lobby.append(Speedy())

class HeavyWave(Wave):

    def fill(self):
        for _ in range(5):
            self.lobby.append(Tank())