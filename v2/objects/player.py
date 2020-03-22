import pyxel

from objects.rectangle import Rectangle

class Player(Rectangle):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.dynamic_entity = True
        self.gravity = True

        self.collision_check_area = Rectangle(
            self.x - (self.w * 3 / 2 - self.w / 2),
            self.y - (self.h * 3 / 2 - self.h / 2),
            self.w * 3,
            self.h * 3
        )

        self.dx = 0
        self.dy = 0

    def update(self):
        # if pyxel.btn(pyxel.KEY_W):
        #     self.y -= 1

        if pyxel.btn(pyxel.KEY_A):
            self.x -= 1

        if pyxel.btn(pyxel.KEY_D):
            self.x += 1

        self.y += self.dy

        self.collision_check_area.x = self.x - (self.w * 3 / 2 - self.w / 2)
        self.collision_check_area.y = self.y - (self.h * 3 / 2 - self.h / 2)

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 7)