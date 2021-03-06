import pyxel
import random
import time

from config import config
from collections import deque, namedtuple
from utility import AABB_collision

Rectangle = namedtuple("Rectangle", ["x", "y", "w", "h"])

class qtree:
    def __init__(self, bounds, capacity):
        self.bounds = bounds
        self.capacity = capacity

        self.divided = False

        self.objs = deque()

    def insert(self, obj):
        if not AABB_collision(self.bounds, obj, include_borders=True):
            return False

        if len(self.objs) < self.capacity:
            self.objs.append(obj)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.top_left.insert(obj):
                return True
            elif self.top_right.insert(obj):
                return True
            elif self.bottom_left.insert(obj):
                return True
            elif self.bottom_right.insert(obj):
                return True
    
    def subdivide(self):
        bx = self.bounds.x
        by = self.bounds.y
        bw = self.bounds.w
        bh = self.bounds.h

        top_left_area = Rectangle(
            x=bx,
            y=by,
            w=bw / 2,
            h=bh / 2
        )
        self.top_left = qtree(top_left_area, self.capacity)

        top_right_area = Rectangle(
            x=bx + bw / 2,
            y=by,
            w=bw / 2,
            h=bh / 2
        )
        self.top_right = qtree(top_right_area, self.capacity)

        bottom_left_area = Rectangle(
            x=bx,
            y=by + bh / 2,
            w=bw / 2,
            h=bh / 2
        )
        self.bottom_left = qtree(bottom_left_area, self.capacity)

        bottom_right_area = Rectangle(
            x=bx + bw / 2,
            y=by + bh / 2,
            w=bw / 2,
            h=bh / 2
        )
        self.bottom_right = qtree(bottom_right_area, self.capacity)

        self.divided = True

    def query(self, area):
        objects_founded = []

        if not AABB_collision(self.bounds, area):
            return objects_founded

        for obj in self.objs:
            if AABB_collision(area, obj, include_borders=True):
                objects_founded.append(obj)

        if self.divided:
            objects_founded += self.top_left.query(area)
            objects_founded += self.top_right.query(area)
            objects_founded += self.bottom_left.query(area)
            objects_founded += self.bottom_right.query(area)

        return objects_founded
    
    def debug_fill(self):
        random.seed(5)

        for x in range(20):
            debug_rect = Rectangle( 
                x=random.randint(0, config['width']),
                y=random.randint(0, config['height']),
                w=15,
                h=15
            )

            self.insert(debug_rect);
    
    def debug_draw(self):

        if self.divided:
            self.top_left.debug_draw()
            self.top_right.debug_draw()
            self.bottom_left.debug_draw()
            self.bottom_right.debug_draw()

        if config["qtree_debug_obj"]:
            for obj in self.objs:
                pyxel.rectb(obj.x, obj.y, obj.w, obj.h, 3)

        if config['qtree_debug_bounds']:
            pyxel.rectb(
                self.bounds.x, 
                self.bounds.y, 
                self.bounds.w, 
                self.bounds.h, 
                8
            )
            pyxel.text(self.bounds.x + self.bounds.w / 2, self.bounds.y + self.bounds.h / 2, str(len(self.objs)), 7)