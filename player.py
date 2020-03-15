import pyxel

from entity_config import e_config
from config import config

from entity import Entity

class Player(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.type = e_config['types']['player']
        self.check_collision = True

        self.speed = 2

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

        self.collision_directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
        }

        self.overlap_list = [
            'ladderE',
            'ladderX'
        ]

        self.is_colliding = False

        self.current_directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
        }

    def update(self):
        self.key_handling()

        moved = False

        if self.current_directions['up'] and not self.collision_directions['up']:
            self.y -= self.speed
            moved = True

        if self.current_directions['down'] and not self.collision_directions['down']:
            self.y += self.speed
            moved = True

        if self.current_directions['right'] and not self.collision_directions['right']:
            self.x += self.speed
            moved = True

        if self.current_directions['left'] and not self.collision_directions['left']:
            self.x -= self.speed
            moved = True

        if moved:
            if self.is_colliding:
                for key in self.current_directions.keys():
                    if self.current_directions[key]:
                        self.collision_directions[key] = False

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

    def key_handling(self):
        if pyxel.btn(pyxel.KEY_W):
            self.current_directions['up'] = True

        if pyxel.btn(pyxel.KEY_S):
            self.current_directions['down'] = True
            
        if pyxel.btn(pyxel.KEY_D):
            self.current_directions['right'] = True

        if pyxel.btn(pyxel.KEY_A):
            self.current_directions['left'] = True

        if pyxel.btnr(pyxel.KEY_W):
            self.current_directions['up'] = False

        if pyxel.btnr(pyxel.KEY_S):
            self.current_directions['down'] = False
            
        if pyxel.btnr(pyxel.KEY_D):
            self.current_directions['right'] = False

        if pyxel.btnr(pyxel.KEY_A):
            self.current_directions['left'] = False