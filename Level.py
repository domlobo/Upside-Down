try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Background import Background
from Enemy import BasicEnemy
from PlayerEnemyInteraction import PlayerEnemyInteraction
from Vector import Vector
import GV

class Level:

    def __init__(self, backgroundURL, foregroundURL, cloudsURL, player):
        self.background = Background(backgroundURL, foregroundURL, cloudsURL)
        self.enemies = [BasicEnemy(Vector((600, GV.CANVAS_HEIGHT / 2)), 100, player), BasicEnemy(Vector((800, GV.CANVAS_HEIGHT / 2)), 100, player)]
        self.collInter = PlayerEnemyInteraction(player, self.enemies)
