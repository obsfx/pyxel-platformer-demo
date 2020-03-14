import pyxel
import random

from collections import namedtuple
from qtree import CenteredRectangle, qtree

init_args = {
    'width': 176,
    'height': 256,
    'caption': "here we go",
    'fps': 50
}

c_qtree = qtree(
    CenteredRectangle(
        x=init_args['width'] / 2,
        y=init_args['height'] / 2,
        w=init_args['width'] / 2,
        h=init_args['height'] / 2
    ),
    capacity=4
)

Prop_Obj = namedtuple("Prop_Obj", ["x", "y", "w", "h"])

for x in range(300):
    c_qtree.insert(
        Prop_Obj(
            x=random.randint(0, init_args['width']),
            y=random.randint(0, init_args['height']),
            w=2,
            h=2
        )
    );

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

        pyxel.run(self.update, self.draw)

    def update(self):
        print("test update")
    
    def draw(self):
        pyxel.cls(0)
        c_qtree.debug_draw()

App()