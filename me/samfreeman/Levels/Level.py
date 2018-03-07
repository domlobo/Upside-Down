try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameObject.PlayerEnemyInteraction import PlayerEnemyInteraction
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.Helper.Display import DisplayBar
from me.samfreeman.Helper.Background import Background
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite

class Level:

    def __init__(self, backgroundURL, foregroundURL, cloudsURL, player,inter, name):
        self.background = Background(backgroundURL, foregroundURL, cloudsURL)
        self.enemies = []
        self.objects = []
        self.player = player
        self.inter = inter
        self.displayBar = DisplayBar(name, self.player.health, self.player.weapon)

    #load the enemies into the class
    def loadEnemies(self, fileLocation):
        file = open(fileLocation, "r")
        #load all the enemies in
        for line in file:
            if line == "Walls\n":
                break
            #arg[0] is x pos, arg[1] is health
            args = line.split(",")
            self.enemies.append(BasicEnemy(Vector((int(args[0]), GV.CANVAS_HEIGHT - 131)),int(args[1]),self.player))
        #load all the objects
        for line in file:
            #arg[0] is image path, arg[1] is x pos, arg[2] is y pos
            args = line.split(",")
            objectSprite = Sprite(args[0])
            self.objects.append(GameObject(Vector((float(args[1]),float(args[2]))), Vector((0,0)), (objectSprite.frameWidth,objectSprite.frameHeight), 100,objectSprite))

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
        for objectOnScreen in self.objects:
            objectOnScreen.draw(canvas, "Purple")
        self.displayBar.drawDisplayBar(canvas)

    #checks for input and collisions
    def update(self):
        self.displayBar.updateBar(self.player.health, self.player.weapon)
        self.inter.checkProjectileCollision(self.enemies,self.player)
        self.inter.checkKeyboard()
        #update the location of all of the elements if the canvas is moving
        if (self.background.foregroundVel.x !=0):
            for proj in self.player.projectiles:
                proj.position.add(self.background.foregroundVel)
            for enemy in self.enemies:
                enemy.position.add(self.background.foregroundVel)
            #use objectOnScreen since object is a reserved keyword
            for objectOnScreen in self.objects:
                objectOnScreen.position.add(self.background.foregroundVel)


    #returns the player so they can be passed on to next level
    def returnPlayer(self):
        return self.player

    #returns true if level is over
    def levelComplete(self):
        #check if the character is in the last x number of pixels of the screen
        return(not self.background.isStillRunning()) and (self.player.position.x > GV.CANVAS_WIDTH - 70)
