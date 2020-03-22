import pyxel
import random
import time

import globals

from entity_config import tmi
from config import config
from utility import get_key

from world import World

from player import Player
from obj import Obj
from enemy import Enemy

class Game:
    def __init__(self):
        self.world = World()

        self.current_tm = 0

        self.tm_offsetX = 16
        self.tm_offsetY = 0

        self.world.push(Player(30, 30, 8, 8))
        self.world.push(Enemy(30, 110, 8, 8, 5))

        self.push_the_objects()
    def update(self):

        if globals.shake_duration > 0:
            globals.camX = random.randint(-1, 1) + random.randint(-globals.camShakeX, globals.camShakeX)
            globals.camY = random.randint(-1, 1) + random.randint(-globals.camShakeY, globals.camShakeY)
            globals.shake_duration -= 0.1
        else:
            globals.camX = 0
            globals.camY = 0

        self.world.update()
        self.world.check_collisions()

        if config['debug']:
            self.world.debug_update()

    def draw(self):
        pyxel.bltm(globals.camX, globals.camY, self.current_tm, self.tm_offsetX, self.tm_offsetY, config['width'], config['height'], 0)

        self.world.draw()

        if config['debug']:
            self.world.debug_draw()

    def push_the_objects(self):
        tmi_values = tmi.values()

        for i in range(config['height'] // 8):
            for j in range(config['width'] // 8):
                data = pyxel.tilemap(self.current_tm).get(j + self.tm_offsetX, i + self.tm_offsetY)
                
                if data in tmi_values:
                    self.world.push(Obj(j * 8, i * 8, 8, 8, get_key(tmi, data)[0]))