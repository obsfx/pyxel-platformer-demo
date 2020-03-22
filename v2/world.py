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
            if entity.gravity:
                entity.dy += self.gravity

            entity.update()

            self.qtree.insert(entity)

        for entity in entities:
            if entity.dynamic_entity:
                entities_in_collision_area = self.qtree.query(entity.collision_check_area)
                
                for entity_ica in entities_in_collision_area:
                    if collision.check(entity, entity_ica):
                        new_entity_pos = collision.resolve(entity, entity_ica)

                        entity.x = new_entity_pos[0]
                        entity.y = new_entity_pos[1]

        return entities