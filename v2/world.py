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

                left = False
                right = False
                top = False
                bottom = False

                for entity_ica in entities_in_collision_area:
                    if entity != entity_ica:

                        if collision.check(entity, entity_ica):
                            resolved_collision = collision.resolve(entity, entity_ica)

                            entity.x = resolved_collision.x
                            entity.y = resolved_collision.y

                            if resolved_collision.left:
                                left = True

                            if resolved_collision.right:
                                right = True

                            if resolved_collision.top:
                                top = True

                            if resolved_collision.bottom:
                                bottom = True
                print(left, right, top, bottom)

                entity.left_collided = left
                entity.right_collided = right
                entity.top_collided = top
                entity.bottom_collided = bottom

        return entities