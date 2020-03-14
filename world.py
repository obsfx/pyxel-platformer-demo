import pyxel

from config import config
from collections import deque
from qtree import Rectangle, qtree

class World:
    def __init__(self):
        self.qtree = []
        self.objects = deque()

        if config['debug']:
            self.qtree_area = {
                "x": 0, 
                "y": 0, 
                "w": 40, 
                "h": 40
            }
            self.debug_founded_objs_in_area = []

    def push(self, obj):
        self.objects.append(obj)
    
    def pop(self, obj):
        self.objects.remove(obj)

    def update(self):

        self.qtree = qtree(
            Rectangle(
                x=0,
                y=0,
                w=config['width'],
                h=config['height']
            ),
            capacity=4
        )

        for obj in self.objects:
            obj.update()

            if obj.id == "player":
                print(obj.x, obj.y)
                
            self.qtree.insert(obj)

    def draw(self):
        for obj in self.objects:
            obj.draw()

    def debug_update(self):
        if config["qtree_debug_fill"]:
            self.qtree.debug_fill()

        self.qtree_area["x"] = pyxel.mouse_x
        self.qtree_area["y"] = pyxel.mouse_y

        debug_rect = Rectangle(
            x=self.qtree_area["x"] - self.qtree_area["w"] / 2, 
            y=self.qtree_area["y"] - self.qtree_area["h"] / 2, 
            w=self.qtree_area["w"], 
            h=self.qtree_area["h"]
        )

        self.debug_founded_objs_in_area = self.qtree.query(debug_rect)

    def debug_draw(self):
        self.qtree.debug_draw()

        pyxel.rectb(
            self.qtree_area["x"] - self.qtree_area["w"] / 2, 
            self.qtree_area["y"] - self.qtree_area["h"] / 2, 
            self.qtree_area["w"], 
            self.qtree_area["h"], 
            11
        )

        for obj in self.debug_founded_objs_in_area:
            pyxel.rect(
                obj.x, 
                obj.y, 
                obj.w, 
                obj.h, 
                7
            )

        pyxel.text(0, 0, str(len(self.debug_founded_objs_in_area)), 12)