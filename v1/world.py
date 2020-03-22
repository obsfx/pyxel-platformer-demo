import pyxel
import math
import random

import globals

from config import config
from entity_config import e_config
from qtree import Rectangle, qtree
from utility import AABB_collision, create_particles

from particle import Particle

class World:
    def __init__(self):
        self.qtree = []
        self.objects = []
        self.gravity = 0.15

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

    def update(self):
        if config['qtree_debug_area']:
            self.debug_founded_objs_in_area = []

        self.objects += globals.bullets
        globals.bullets = []

        self.objects += globals.particles
        globals.particles = []

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

            if obj.gravity and not obj.is_climbing:
                obj.y += obj.dy
                obj.dy += self.gravity

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

                obj.is_colliding = False
                obj.grounded = False

                obj.collision_directions['up'] = False
                obj.collision_directions['down'] = False
                obj.collision_directions['right'] = False
                obj.collision_directions['left'] = False

                collisions = {
                    'left': False,
                    'right': False,
                    'up': False,
                    'down': False
                }

                
                for obj_in_area in objects_in_area:
                    if (obj != obj_in_area and obj_in_area.id in obj.collision_list):
                        
                        # print(math.atan2(dy, dx) * (180 / math.pi) + 180)

                        

                        # left 45 - 0 360 - 315
                        # bottom 315 - 225
                        # right 225 - 135
                        # top 135 - 45

                        if AABB_collision(obj, obj_in_area):
                            #print("collision!!")
                            obj.is_colliding = True

                            if (obj.id == 'Bullet'):
                                pc = 5
                                b = False
                                
                                if obj_in_area.id in globals.blood_p:
                                    pc = 8
                                    b = True

                                create_particles(obj, pc * 2, pc, b)
                                if obj in self.objects:
                                    self.objects.remove(obj)
                            
                            # dx = obj.x - obj.sx - obj_in_area.x
                            # dy = obj.y - obj.dy - obj_in_area.y

                            dx = (obj.x + obj.w / 2) - obj.sx - (obj_in_area.x + obj_in_area.w / 2)
                            dy = (obj.y + obj.h / 2) - obj.dy - (obj_in_area.y + obj_in_area.h / 2)

                            dis = math.sqrt(dx * dx + dy * dy)
                            deg = math.atan2(dy, dx) * (180 / math.pi) + 180

                            if deg >= 45 and deg <= 135:
                                # print('bottom')
                                collisions['down'] = True

                            if deg >= 225 and deg <= 315:
                                print('top')
                                collisions['up'] = True
                                obj.collision_directions['up'] = True
                                obj.dy *= -1
                                obj.y += obj.dy

                            if deg >= 135 and deg <= 225:
                                # print('left')
                                collisions['left'] = True

                            if (deg >= 0 and deg <= 45) or (deg >= 315 and deg <= 360):
                                # print('right')
                                collisions['right'] = True

                            if collisions['down'] and obj.current_directions['down']:
                                obj.collision_directions['down'] = True
                                # print('down')

                            if collisions['right'] and obj.current_directions['right']:
                                obj.collision_directions['right'] = True
                                # print('right')

                            if collisions['left'] and obj.current_directions['left']:
                                obj.collision_directions['left'] = True
                                # print('left')

                            if obj.collision_directions['up'] and obj.y % 8 != 0:
                                obj.y += obj.dy

                            if obj.collision_directions['down'] and obj.y % 8 != 0:
                                obj.y -= obj.y % 8

                            if obj.collision_directions['right'] and obj.x % 8 != 0:
                                obj.x -= obj.x % 8

                            if obj.collision_directions['left'] and obj.x % 8 != 0:
                                obj.x += 8 - (obj.x % 8)

                            if collisions['down']:
                                if obj.gravity and not obj.grounded:
                                    if obj.id != 'Particle':
                                        obj.y -= obj.y % 8
                                    elif obj.id == 'Particle':
                                        obj.sx = 0
                                        obj.check_collision = False
                                        obj.gravity = False
                                        #print(obj.id)

                                    obj.dy -= obj.dy
                                    obj.grounded = True

                    if (obj != obj_in_area and obj_in_area.id in obj.overlap_list):
                        # if (obj_in_area.id == "ladderQ"):
                        #     print(dis)
                        dx = (obj.x + obj.w / 2) - obj.sx - (obj_in_area.x + obj_in_area.w / 2)
                        dy = (obj.y + obj.h / 2) - obj.dy - (obj_in_area.y + obj_in_area.h / 2)
                        dis = math.sqrt(dx * dx + dy * dy)
                        if dis < 11:
                            obj.overlap_action(obj_in_area, dis)

                if config['qtree_debug_area']:
                    self.debug_founded_objs_in_area += objects_in_area

    ## ----------------------------------------------------

    def debug_update(self):
        if config["qtree_debug_fill"]:
            self.qtree.debug_fill()

        if config['qtree_debug_area']:
            self.qtree_area["x"] = pyxel.mouse_x
            self.qtree_area["y"] = pyxel.mouse_y

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
                self.qtree_area['x'] - self.qtree_area['w'] / 2 + globals.camX, 
                self.qtree_area['y'] - self.qtree_area['h'] / 2 + globals.camY,  
                self.qtree_area['w'], 
                self.qtree_area['h'], 
                11
            )

            for obj in self.debug_founded_objs_in_area:
                pyxel.rect(
                    obj.x + globals.camX, 
                    obj.y + globals.camY, 
                    obj.w, 
                    obj.h, 
                    7
                )

            pyxel.text(0 + globals.camX, 0 + globals.camY, str(len(self.debug_founded_objs_in_area)), 12)