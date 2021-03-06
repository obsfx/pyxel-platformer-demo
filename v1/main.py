import pyxel

from config import config
from game import Game

class App:
    def __init__(self):
        pyxel.init(
            width=config['width'], 
            height=config['height'], 
            caption=config['caption'], 
            fps=config['fps'], 
            scale=config['scale'], 
        )

        pyxel.load('assets/assets.pyxres')

        pyxel.mouse(config['mouse'])

        self.game = Game()
        
        pyxel.run(self.update, self.draw)
    def update(self):
        self.game.update()

    def draw(self):
        pyxel.cls(0)
        self.game.draw()

App()
