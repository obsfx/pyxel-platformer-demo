import pyxel

import globs.config
import globs.camera
import globs.tiles

from objects.entity import Entity

class TileMap:
    def __init__(self, index, offsetx, offsety, tilesize):
        self.index = index
        self.offsetx = offsetx
        self.offsety = offsety
        self.tilesize = tilesize

    def draw(self):
        pyxel.bltm(
            globs.camera.x,
            globs.camera.y,
            self.index,
            self.offsetx,
            self.offsety,
            globs.config.width,
            globs.config.height,
            0
        )

    def get_blocks(self):
        blocks = []

        tile_keys = globs.tiles.data.keys()

        rows = globs.config.height // self.tilesize
        cols = globs.config.width // self.tilesize

        for row in range(rows):
            for col in range(cols):
                tile_id = str(pyxel.tilemap(self.index).get(self.offsetx + col, self.offsety + row))

                if tile_id in tile_keys:
                    tile_data = globs.tiles.data[tile_id]
                    x = col * self.tilesize
                    y = row * self.tilesize
                    w = 8
                    h = 8

                    if type(tile_data) is dict:
                        w = tile_data['hitbox_w']
                        h = tile_data['hitbox_h']

                    blocks.append(Entity(x, y, w, h))

        return blocks