import pyxel
import random
import time

from collections import namedtuple
from qtree import CenteredRectangle, qtree

init_args = {
    'width': 176,
    'height': 256,
    'caption': "here we go",
    'fps': 50
}

Prop_Obj = namedtuple("Prop_Obj", ["x", "y", "w", "h"])

class App:
    def __init__(self):
        pyxel.init(
            width=init_args['width'], 
            height=init_args['height'], 
            caption=init_args['caption'], 
            fps=init_args['fps'], scale=2, 
            border_width=0, 
            border_color=0
        )
        pyxel.mouse(True)

        self.d_area = {
            "x": 0, "y": 0, "w": 20, "h": 20
        }

        self.c_qtree = qtree(
            CenteredRectangle(
                x=init_args['width'] / 2,
                y=init_args['height'] / 2,
                w=init_args['width'] / 2,
                h=init_args['height'] / 2
            ),
            capacity=4
        )

        self.f = []

        for x in range(1200):
            self.c_qtree.insert(
                Prop_Obj(
                    x=random.randint(0, init_args['width']),
                    y=random.randint(0, init_args['height']),
                    w=2,
                    h=2
                )
            );

        pyxel.run(self.update, self.draw)

    def update(self):
        print("test update")
        
        self.d_area["x"] = pyxel.mouse_x
        self.d_area["y"] = pyxel.mouse_y

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            random.seed( time.time() )
            rk = random.randint(2000, 3000)

            self.c_qtree = qtree(
                CenteredRectangle(
                    x=init_args['width'] / 2,
                    y=init_args['height'] / 2,
                    w=init_args['width'] / 2,
                    h=init_args['height'] / 2
                ),
                capacity=4
            )

            for x in range(rk):
                self.c_qtree.insert(
                    Prop_Obj(
                        x=random.randint(0, init_args['width']),
                        y=random.randint(0, init_args['height']),
                        w=2,
                        h=2
                    )
                );

        self.f = self.c_qtree.query(CenteredRectangle(x=self.d_area["x"], y=self.d_area["y"], w=self.d_area["w"], h=self.d_area["h"]))
    
    def draw(self):
        pyxel.cls(0)
        self.c_qtree.debug_draw()

        pyxel.rectb(self.d_area["x"] - self.d_area["w"], self.d_area["y"] - self.d_area["h"], self.d_area["w"] * 2, self.d_area["h"] * 2, 11)

        for o in self.f:
            pyxel.rect(
                o.x - o.w, 
                o.y - o.h, 
                o.w * 2, 
                o.h * 2, 
                7
            )
        pyxel.text(0, 0, str(len(self.f)), 12)

App()