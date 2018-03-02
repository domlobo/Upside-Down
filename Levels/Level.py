try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import GameControl.GV as GV

from GameObject.Enemy import BasicEnemy
from GameObject.PlayerEnemyInteraction import PlayerEnemyInteraction
from Helper.Background import Background
from Helper.Vector import Vector


class Level:

    def __init__(self, backgroundURL, foregroundURL, cloudsURL, player,inter):
        self.background = Background(backgroundURL, foregroundURL, cloudsURL)
        self.enemies = []
        self.collInter = PlayerEnemyInteraction(player, self.enemies)
        self.player = player
        self.inter = inter

    #load the enemies into the class
    def loadEnemies(self, fileLocation):
        file = open(fileLocation, r)
        for line in file:
            self.enemies.add(BasicEnemy(line))

    def setPlayer(self,player):
        self.player = player

    #draws all the entities
    def draw(self, canvas):
        self.update()
        self.background.update(canvas, self.player)
        self.player.draw(canvas, "Green")
        for proj in self.player.projectiles:
            proj.draw(canvas, "Blue")
        for enemy in self.enemies:
            enemy.draw(canvas, "Red")

    #checks for input and collisions
    def update(self):
        self.collInter.update()
        self.inter.checkKeyboard()

    #returns the player so they can be passed on to next level
    def returnPlayer(self):
        return self.player

    #returns true if level is over
    def levelComplete(self):
        #check if the character is in the last 50 pixels of the screen
        return(not self.background.isStillRunning()) and (self.player.position.x > GV.CANVAS_WIDTH - 50)
