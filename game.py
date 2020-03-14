import pyxel

from config import config
from world import World
from player import Player

class Game:
    def __init__(self):
        self.world = World()
        self.player = Player(30, 30, 20, 20)

        self.world.push(self.player)

    def update(self):
        self.world.update()

        if config['debug']:
            self.world.debug_update()

    def draw(self):
        self.world.draw()

        if config['debug']:
            self.world.debug_draw()