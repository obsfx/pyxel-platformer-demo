from objects.rectangle import Rectangle

class Entity(Rectangle):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.active = True
        self.collision = True
        self.overlap = False
        self.dynamic_entity = False
        self.gravity = False

    def update(self):
        pass

    def draw(self):
        pass