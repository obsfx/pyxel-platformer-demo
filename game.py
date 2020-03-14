import pyxel

from config import config
from qtree import CenteredRectangle, qtree

class Game:
    def __init__(self):
        self.qtree = qtree(
            CenteredRectangle(
                x=config['width'] / 2,
                y=config['height'] / 2,
                w=config['width'] / 2,
                h=config['height'] / 2
            ),
            capacity=4
        )
        
        if config['debug']:
            self.qtree.debug_fill()
            self.qtree_area = {
                "x": 0, 
                "y": 0, 
                "w": 20, 
                "h": 20
            }
            self.debug_founded_objs_in_area = []

    def update(self):
        pass

    def draw(self):
        pass
    
    def debug_update(self):
        self.qtree_area["x"] = pyxel.mouse_x
        self.qtree_area["y"] = pyxel.mouse_y

        debug_rect = CenteredRectangle(x=self.qtree_area["x"], y=self.qtree_area["y"], w=self.qtree_area["w"], h=self.qtree_area["h"])
        self.debug_founded_objs_in_area = self.qtree.query(debug_rect);

    def debug_draw(self):
        self.qtree.debug_draw()

        pyxel.rectb(
            self.qtree_area["x"] - self.qtree_area["w"], 
            self.qtree_area["y"] - self.qtree_area["h"], 
            self.qtree_area["w"] * 2, 
            self.qtree_area["h"] * 2, 
            11
        )

        for obj in self.debug_founded_objs_in_area:
            pyxel.rect(
                obj.x - obj.w, 
                obj.y - obj.h, 
                obj.w * 2, 
                obj.h * 2, 
                7
            )

        pyxel.text(0, 0, str(len(self.debug_founded_objs_in_area)), 12)