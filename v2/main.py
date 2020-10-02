import pyxel

import globs.config
import util.debug

from game import Game
class App:
    def __init__(self):
        pyxel.init(
            width=globs.config.width,
            height=globs.config.height,
            caption=globs.config.caption,
            fps=globs.config.fps,
            scale=globs.config.scale,
        )

        pyxel.mouse(globs.config.mouse)
        pyxel.load("assets/assets.pyxres")

        self.game = Game()

        pyxel.run(self.update, self.draw)
    def update(self):
        self.game.update()

    def draw(self):
        pyxel.cls(0)
        self.game.draw()

        if globs.config.debug_tile_data:
            util.debug.tile_data(globs.config.width, globs.config.height, 8, 0, self.game.map.offsetx, self.game.map.offsety)

        if globs.config.debug_entities:
            util.debug.render_bounds(self.game.entities, 7)

        if globs.config.debug_chunk_bounds:
            util.debug.render_bounds(self.game.world.qtree.get_chunks(), 8)

        if globs.config.debug_collision_area:
            util.debug.render_collision_areas(self.game.entities, 7)

App()
