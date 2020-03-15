import pyxel

from entity_config import e_config
from config import config

from entity import Entity

class Player(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.type = e_config['types']['player']
        self.check_collision = True

        self.collision_area = {
            'x': self.x - 14,
            'y': self.y - 14,
            'w': 36,
            'h': 36
        }

        self.collision_list = [
            'block1',
            'block2'
        ]

        self.overlap_list = [
            'ladderE',
            'ladderX'
        ]

    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 1

        if pyxel.btn(pyxel.KEY_S):
            self.y += 1
            
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1

        if pyxel.btn(pyxel.KEY_A):
            self.x -= 1

        # (32 - 8) / 2
        self.collision_area['x'] = self.x - 14
        self.collision_area['y'] = self.y - 14

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 15)

        if config['qtree_debug_area']:
            pyxel.rectb(
                self.collision_area['x'], 
                self.collision_area['y'], 
                self.collision_area['w'], 
                self.collision_area['h'], 
                11
            )