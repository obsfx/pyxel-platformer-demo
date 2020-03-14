import pyxel
import random
import time

from config import config
from world import World
from player import Player
from obj import Obj

class Game:
    def __init__(self):
        self.world = World()

        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))
        self.world.push(Player(30, 30, 10, 10))

        random.seed(3)
        random.seed(time.time())

        for x in range(50):
            self.world.push(Obj(
                random.randint(0, config["width"]),
                random.randint(0, config["height"]),
                15,
                15
            ))

    def update(self):
        self.world.update()

        if config['debug']:
            self.world.debug_update()

    def draw(self):
        self.world.draw()

        if config['debug']:
            self.world.debug_draw()