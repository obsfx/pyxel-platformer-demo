import pyxel

from collections import deque, namedtuple

# class centered_rectangle:
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius

CenteredRectangle = namedtuple("CenteredRectangle", ["x", "y", "w", "h"])

class qtree:
    def __init__(self, bounds, capacity):
        self.bounds = bounds
        self.capacity = capacity

        self.divided = False

        self.objs = deque()

    def is_inside(self, obj):
        return (
            obj.x + obj.w >= self.bounds.x - self.bounds.w and
            obj.x <= self.bounds.x + self.bounds.w and
            obj.y + obj.h >= self.bounds.y - self.bounds.h and
            obj.y <= self.bounds.y + self.bounds.h
        )

    def insert(self, obj):
        if not self.is_inside(obj):
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

        top_left_area = CenteredRectangle(
            x=bx - bw / 2,
            y=by - bh / 2,
            w=bw / 2,
            h=bh / 2
        )
        self.top_left = qtree(top_left_area, self.capacity)

        top_right_area = CenteredRectangle(
            x=bx + bw / 2,
            y=by - bh / 2,
            w=bw / 2,
            h=bh / 2
        )
        self.top_right = qtree(top_right_area, self.capacity)

        bottom_left_area = CenteredRectangle(
            x=bx - bw / 2,
            y=by + bh / 2,
            w=bw / 2,
            h=bh / 2
        )
        self.bottom_left = qtree(bottom_left_area, self.capacity)

        bottom_right_area = CenteredRectangle(
            x=bx + bw / 2,
            y=by - bh / 2,
            w=bw / 2,
            h=bh / 2
        )
        self.bottom_right = qtree(bottom_right_area, self.capacity)

        self.divided = True
    
    def debug_draw(self):
        pyxel.rectb(
            self.bounds.x - self.bounds.w, 
            self.bounds.y - self.bounds.h, 
            self.bounds.w * 2, 
            self.bounds.h * 2, 8
        )

        for obj in self.objs:
            pyxel.rect(obj.x, obj.y, obj.w, obj.h, 3)

        if self.divided:
            self.top_left.debug_draw()
            self.top_right.debug_draw()
            self.bottom_left.debug_draw()
            self.bottom_right.debug_draw()