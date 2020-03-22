from collections import deque, namedtuple

import modules.collision as collision
from objects.rectangle import Rectangle

class QTree(Rectangle):
    def __init__(self, x, y, w, h, capacity):
        super().__init__(x, y, w, h)

        self.capacity = capacity

        self.divided = False

        self.entities = deque()

    def insert(self, obj):
        if not collision.check(self, obj, include_borders=True):
            return False

        if len(self.entities) < self.capacity:
            self.entities.append(obj)
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
        bx = self.x
        by = self.y
        bw_h = self.w / 2
        bh_h = self.h / 2

        self.top_left = QTree(bx, by, bw_h, bh_h, self.capacity)
        self.top_right = QTree(bx + bw_h, by, bw_h, bh_h, self.capacity)
        self.bottom_left = QTree(bx, by + bh_h, bw_h, bh_h, self.capacity)
        self.bottom_right = QTree(bx + bw_h, by + bh_h, bw_h, bh_h, self.capacity)

        self.divided = True

    def query(self, area):
        entities = deque()

        if not collision.check(self, area):
            return entities

        for entity in self.entities:
            if collision.check(entity, area, include_borders=True):
                entities.append(entity)
        
        if self.divided:
            entities += self.top_left.query(area)
            entities += self.top_right.query(area)
            entities += self.bottom_left.query(area)
            entities += self.bottom_right.query(area)

        return entities

    def get_chunks(self):
        chunks = deque()

        chunks.append(self)

        if self.divided:
            chunks += self.top_left.get_chunks()
            chunks += self.top_right.get_chunks()
            chunks += self.bottom_left.get_chunks()
            chunks += self.bottom_right.get_chunks()

        return chunks

    def get_all_entities(self):
        entities = deque()

        entities += self.entities

        if self.divided:
            entities += self.top_left.get_all_entities()
            entities += self.top_right.get_all_entities()
            entities += self.bottom_left.get_all_entities()
            entities += self.bottom_right.get_all_entities()

        return entities