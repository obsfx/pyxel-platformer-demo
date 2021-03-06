import pyxel
import globals

from entity_config import e_config
from config import config
from obj import Obj

class Bullet(Obj):
    def __init__(self, x, y, xvel, col):
        super().__init__(x, y, 2, 2, 'Bullet')
        self.sx = xvel
        self.dy = 0

        self.col = col
        
        
        self.check_collision = True
        self.is_colliding = False

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
        if self.current_directions['left']:
            self.sx -= 0.25
        else:
            self.sx += 0.25
        self.x += self.sx

        self.collision_area['x'] = self.x - 7
        #self.collision_area['y'] = self.y - 14
    
    def draw(self):
        # pyxel.rect(self.x + globals.camX, self.y + globals.camY, self.w, self.h, self.col)
        if self.current_directions['left']:
            pyxel.blt(self.x + globals.camX, self.y + globals.camY, 0, 48, 0, 8, 8, 0)
        else:
            pyxel.blt(self.x + globals.camX, self.y + globals.camY, 0, 40, 0, 8, 8, 0)

        if config['qtree_debug_area']:
            pyxel.rectb(
                self.collision_area['x'] + globals.camX, 
                self.collision_area['y'] + globals.camY, 
                self.collision_area['w'], 
                self.collision_area['h'], 
                11
            )