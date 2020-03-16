import pyxel

from entity_config import e_config
from config import config

from entity import Entity

class Player(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

        self.type = e_config['types']['player']
        self.check_collision = True
        self.gravity = True
        self.grounded = False

        self.is_colliding = False
        self.is_climbing = False

        self.speed = 2
        self.dy = 0.1
        self.acceleration = 0.1

        self.sx = 0
        self.sy = 0

        self.collision_area = {
            'x': self.x - 14,
            'y': self.y - 14,
            'w': 36,
            'h': 36
        }

        # self.ground_area = {
        #     'x': self.x,
        #     'y': self.y + 6,
        #     'w': 8,
        #     'h': 6
        # }

        self.collision_list = [
            'block1',
            'block2',
            'ladderQ'
        ]

        self.collision_directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
        }

        self.overlap_list = [
            'ladderQ',
            'ladderE',
            'ladderB'
        ]

        self.toggle_overlaps = {
            'ladderQ': True
        }

        self.current_directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False
        }

        self.pressed = {
            'e': False
        }

        self.locked = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
            'e': False
        }

    def update(self):
        self.key_handling()
        # print(self.x, self.y)

        self.sx = 0

        if self.current_directions['up'] and not self.collision_directions['up'] and self.grounded and not self.locked['up']:
            # self.y -= self.speed
            self.dy = -1.95
            self.locked['up'] = True

        if self.is_climbing and self.current_directions['up'] and not self.collision_directions['up']:
            self.y -= self.speed / 2

        if self.current_directions['down'] and not self.collision_directions['down'] and self.is_climbing:
            self.y += self.speed / 2

        if self.current_directions['right'] and not self.collision_directions['right']:
            self.sx = self.speed

        if self.current_directions['left'] and not self.collision_directions['left']:
            self.sx = -self.speed

        if not self.is_climbing:
            self.x += self.sx
        # if moved:
        #     if self.is_colliding:
        #         for key in self.current_directions.keys():
        #             if self.current_directions[key]:
        #                 self.collision_directions[key] = False

        # (32 - 8) / 2
        self.collision_area['x'] = self.x - 14
        self.collision_area['y'] = self.y - 14

        # self.ground_area['x'] = self.x
        # self.ground_area['y'] = self.y + 6

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 15)
        pyxel.text(self.x + self.w / 2, self.y + self.h / 2, str(self.x), 8)
        pyxel.text(self.x + self.w / 2, self.y + self.h / 2 + 5, str(self.y), 8)

        if config['qtree_debug_area']:
            pyxel.rectb(
                self.collision_area['x'], 
                self.collision_area['y'], 
                self.collision_area['w'], 
                self.collision_area['h'], 
                11
            )

            # pyxel.rectb(
            #     self.ground_area['x'], 
            #     self.ground_area['y'], 
            #     self.ground_area['w'], 
            #     self.ground_area['h'], 
            #     10
            # )

    def key_handling(self):
        if pyxel.btn(pyxel.KEY_W):
            self.current_directions['up'] = True

        if pyxel.btn(pyxel.KEY_E):
            self.pressed['e'] = True

        if pyxel.btn(pyxel.KEY_S):
            self.current_directions['down'] = True
            
        if pyxel.btn(pyxel.KEY_D):
            self.current_directions['right'] = True

        if pyxel.btn(pyxel.KEY_A):
            self.current_directions['left'] = True

        if pyxel.btnr(pyxel.KEY_W):
            self.current_directions['up'] = False
            self.locked['up'] = False

        if pyxel.btnr(pyxel.KEY_S):
            self.current_directions['down'] = False
            
        if pyxel.btnr(pyxel.KEY_D):
            self.current_directions['right'] = False

        if pyxel.btnr(pyxel.KEY_A):
            self.current_directions['left'] = False

        if pyxel.btnr(pyxel.KEY_E):
            self.pressed['e'] = False
            self.locked['e'] = False

    def overlap_action(self, obj, dis):
        # print(obj.id)
        # ladderQ
        if obj.id == 'ladderQ':
            if self.pressed['e'] and not self.locked['e']:
                print('tick')
                self.locked['e'] = True

                if self.toggle_overlaps['ladderQ']:
                    self.collision_list.remove('ladderQ')
                    self.toggle_overlaps['ladderQ'] = False
                    self.x = obj.x
                    self.y = obj.y + obj.h / 3
                    self.is_climbing = True
                else:
                    if dis < 4:
                        self.collision_list.append('ladderQ')
                        self.toggle_overlaps['ladderQ'] = True
                        self.x = obj.x
                        self.y = obj.y - self.h
                        self.is_climbing = False

            
            if self.is_climbing:
                if self.y < obj.y:
                    self.y = obj.y

        if obj.id == 'ladderE':
            if self.pressed['e'] and not self.locked['e']:
                self.locked['e'] = True
                if self.is_climbing:
                    self.collision_list.append('ladderQ')
                    self.toggle_overlaps['ladderQ'] = True
                    self.is_climbing = False
                else:
                    if dis < 4:
                        self.collision_list.remove('ladderQ')
                        self.toggle_overlaps['ladderQ'] = False
                        self.x = obj.x
                        self.y = obj.y - obj.h / 3
                        self.is_climbing = True