import pyxel
import globals

from entity_config import e_config
from config import config

from player import Player
from bullet import Bullet
from obj import Obj

class Enemy(Player):
    def __init__(self, x, y, w, h, level):
        super().__init__(x, y, w, h, 'Enemy')
        self.level = level
        self.type = e_config['types']['enemy']
        self.col = 11

        self.overlap_list = []

    def key_handling(self):
        pass
    
    def overlap_action(self, obj, dis):
        pass