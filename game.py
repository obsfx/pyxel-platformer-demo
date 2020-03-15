import pyxel
import random
import time

from entity_config import tmi
from config import config
from utility import get_key

from world import World

from player import Player
from obj import Obj

class Game:
    def __init__(self):
        self.world = World()

        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))
        # self.world.push(Player(30, 30, 10, 10))

        # random.seed(3)
        # random.seed(time.time())

        # for x in range(50):
        #     self.world.push(Obj(
        #         random.randint(0, config['width']),
        #         random.randint(0, config['height']),
        #         15,
        #         15
        #     ))

        tm = []
        tmi_values = tmi.values()

        for i in range(config['height'] // 8):
            tm.append([])
            for j in range(config['width'] // 8):
                d = pyxel.tilemap(0).get(j, i)
                tm[i].append(d)

                if d in tmi_values:
                    self.world.push(Obj(j * 8, i * 8, 8, 8, get_key(tmi, d)[0]))

        print(*tm, sep="\n")
        print(pyxel.tilemap(0).get(5, 4))
        print(tmi_values)

        print(get_key(tmi, 35)[0])
    def update(self):
        self.world.update()

        if config['debug']:
            self.world.debug_update()

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, config['width'], config['height'], 0)

        self.world.draw()

        if config['debug']:
            self.world.debug_draw()