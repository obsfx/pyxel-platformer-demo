import pyxel

from entity_config import e_config
from entity import Entity

class Player(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.type = e_config['types']['player']

    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 1

        if pyxel.btn(pyxel.KEY_S):
            self.y += 1
            
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1

        if pyxel.btn(pyxel.KEY_A):
            self.x -= 1

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 15)