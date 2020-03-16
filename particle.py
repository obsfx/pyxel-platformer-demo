import pyxel
import random
import globals

from entity_config import e_config
from config import config
from obj import Obj

class Particle(Obj):
    def __init__(self, x, y, xvel, col):
        super().__init__(x, y, 1, 1, 'Particle')
        self.sx = xvel
        self.dy = -random.randint(10, 50) / 10

        self.col = col

        self.check_collision = True
        self.gravity = True
        self.grounded = False
        self.is_colliding = False
        self.is_climbing = False

        self.collision_area = {
            'x': self.x - 7,
            'y': self.y - 7,
            'w': 16,
            'h': 16
        }

        self.collision_list = [
            'block1',
            'block2',
        ]

        self.overlap_list = [

        ]

        self.collision_directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
        }

        self.current_directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
        }

        if self.sx < 0:
            self.current_directions['left'] = True
        elif self.sx > 0:
            self.current_directions['right'] = True

    def update(self):
        self.sx += self.current_directions['left'] if 0.2 else -0.2
        self.x += self.sx

        self.collision_area['x'] = self.x - 7
        #self.collision_area['y'] = self.y - 14
    
    def draw(self):
        pyxel.rect(self.x + globals.camX, self.y + globals.camY, self.w, self.h, self.col)

        if config['qtree_debug_area']:
            pyxel.rectb(
                self.collision_area['x'] + globals.camX, 
                self.collision_area['y'] + globals.camY, 
                self.collision_area['w'], 
                self.collision_area['h'], 
                11
            )