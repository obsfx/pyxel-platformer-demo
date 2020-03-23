from collections import deque

from modules.qtree import QTree
import modules.collision as collision

class World:
    def __init__(self, gravity, width, height):
        self.gravity = gravity
        
        self.width = width
        self.height = height

        self.qtree = QTree(0, 0, self.width, self.height, 4)

    def operate(self, entities):
        self.qtree = QTree(0, 0, self.width, self.height, 4)
        
        for entity in entities:
            if entity.gravity and not entity.grounded:
                entity.dy += self.gravity

            entity.update()

            self.qtree.insert(entity)

        for entity in entities:
            if entity.dynamic_entity:
                entities_in_collision_area = self.qtree.query(entity.collision_check_area)
                for entity_ica in entities_in_collision_area:
                    if entity != entity_ica:
                        if collision.check(entity, entity_ica):
                            resolved_collision = collision.resolve(entity, entity_ica)
                            # print(resolved_collision.left, resolved_collision.right, resolved_collision.top, resolved_collision.bottom)
                            entity.set_resolved(resolved_collision)

        return entities