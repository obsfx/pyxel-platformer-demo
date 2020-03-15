import pyxel

from collections import deque

from config import config
from entity_config import e_config
from qtree import Rectangle, qtree
from utility import AABB_collision

class World:
    def __init__(self):
        self.qtree = []
        self.objects = deque()

        if config['debug'] and config['qtree_debug_area']:
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
        if config['qtree_debug_area']:
            self.debug_founded_objs_in_area = []

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
            self.qtree.insert(obj)

            # if obj.type == e_config['types']['player'] and config['debug']:
            #     # self.qtree_area['x'] = obj.x + obj.w / 2
            #     # self.qtree_area['y'] = obj.y + obj.h / 2
            #     print(obj.x, obj.y)

    def draw(self):
        for obj in self.objects:
            obj.draw()

    def check_collisions(self):
        for obj in self.objects:
            if obj.check_collision:
                col_check_area = Rectangle(
                    x=obj.collision_area['x'], 
                    y=obj.collision_area['y'], 
                    w=obj.collision_area['w'], 
                    h=obj.collision_area['h']
                )

                objects_in_area = self.qtree.query(col_check_area)
                
                for obj_in_area in objects_in_area:
                    if (obj != obj_in_area and obj_in_area.id in obj.collision_list):
                        if AABB_collision(obj, obj_in_area):
                            print("collision!!")

                if config['qtree_debug_area']:
                    self.debug_founded_objs_in_area += objects_in_area

    ## ----------------------------------------------------

    def debug_update(self):
        if config["qtree_debug_fill"]:
            self.qtree.debug_fill()

        self.qtree_area["x"] = pyxel.mouse_x
        self.qtree_area["y"] = pyxel.mouse_y

        if config['qtree_debug_area']:
            debug_rect = Rectangle(
                x=self.qtree_area['x'] - self.qtree_area['w'] / 2, 
                y=self.qtree_area['y'] - self.qtree_area['h'] / 2, 
                w=self.qtree_area['w'], 
                h=self.qtree_area['h']
            )

            self.debug_founded_objs_in_area += self.qtree.query(debug_rect)

    def debug_draw(self):
        self.qtree.debug_draw()

        if config['qtree_debug_area']:
            pyxel.rectb(
                self.qtree_area['x'] - self.qtree_area['w'] / 2, 
                self.qtree_area['y'] - self.qtree_area['h'] / 2, 
                self.qtree_area['w'], 
                self.qtree_area['h'], 
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