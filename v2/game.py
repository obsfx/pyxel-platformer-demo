import pyxel

from collections import deque

import globs.config
import globs.camera

from world import World
from tilemap import TileMap
from objects.player import Player
from objects.entity import Entity

class Game:
    def __init__(self):
        self.entities = deque()
        self.map = TileMap(0, 16, 0, 8)
        self.world = World(0.15, globs.config.width, globs.config.height)

        self.entities += self.map.get_blocks()
        
        self.entities.append(Player(8, 12, 8, 12))

        # self.entities.append(Entity(16, 20, 8, 8))
    def update(self):
        if globs.camera.duration > 0:
            globs.camera.duration -= 1
            globs.camera.shake()

        self.entities = self.world.operate(self.entities)

    def draw(self):
        self.map.draw()

        for entity in self.entities:
            entity.draw()

        # pyxel.rect(16, 20, 8, 8, 8)