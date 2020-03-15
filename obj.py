import pyxel

from entity_config import e_config
from entity import Entity

class Obj(Entity):
    def __init__(self, x, y, w, h, _id):
        super().__init__(x, y, w, h)

        self.id = _id
        self.type = e_config['types']['object'] 

    def update(self):
        pass

    def draw(self):
        pass
        # pyxel.rect(self.x, self.y, self.w, self.h, 10)