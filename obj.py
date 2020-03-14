import pyxel

from entity import Entity

class Obj(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def update(self):
        pass

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 10)