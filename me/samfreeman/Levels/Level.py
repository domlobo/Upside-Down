try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.GameObject.StaticEnemy import StaticEnemy
from me.samfreeman.GameObject.LinkBossCharacter import LinkBossCharacter
from me.samfreeman.Helper.Display import DisplayBar
from me.samfreeman.Helper.Background import Background
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.Helper.TextOverlay import TextOverlay

class Level:

    def __init__(self, backgroundURL, foregroundURL, cloudsURL, player,inter, name):
        self.background = Background(backgroundURL, foregroundURL, cloudsURL)
        self.enemies = []
        self.objects = []
        self.player = player
        self.inter = inter
        self.displayBar = DisplayBar(name, self.player.health)

    #load the enemies into the class
    def loadLevelSpecifics(self, fileLocation):
        file = open(fileLocation, "r")
        #load all the text to be displayed
        for line in file:
            #if this section is over, break
            if line == "Enemies\n":
                 break
            #args[0] is speach, args[1] is the speaker
            args = line.split(",")
            self.inter.text.addLine(args[0],args[1][:-1])

        self.inter.text.nextText()
        #load the enemies
        for line in file:
            #if this section is over, break
            if line == "Walls\n":
                break
            #arg[0] is x pos, arg[1] is y pos, arg[2] is health, args[3] and arg[5] are left and right sprites with args[4] and args[6] being the number of colums, args[7] denotes the type of enemy
            args = line.split(",")
            runLeft = Sprite(args[3], True,1,int(args[4]))
            if(args[7] == "d\n"):
                runRight= Sprite(args[5], True,1,int(args[6]))
                self.enemies.append(BasicEnemy(Vector((int(args[0]), int(args[1]))),int(args[2]),self.player, runLeft, runRight))
            elif(args[7] == "s\n"):
                #args[5] and [6] are left blank
                self.enemies.append(StaticEnemy(Vector((int(args[0]), int(args[1]))),int(args[2]),self.player, runLeft))
            elif(args[7] == "bl\n"):
                runRight= Sprite(args[5], True,1,int(args[6]))
                self.enemies.append(LinkBossCharacter(Vector((int(args[0]), int(args[1]))),int(args[2]),self.player, runLeft, runRight))
            elif(args[7] == "bm\n"):
                pass
            elif(args[7] == "bd\n"):
                pass
        #load all the objects
        for line in file:
            if line == "Floor\n":
                break
            #arg[0] is image path, arg[1] is x pos, arg[2] is y pos, args[3] is notCollibable as an int
            args = line.split(",")
            objectSprite = Sprite(args[0])
            print(args[3])
            self.objects.append(GameObject(Vector((float(args[1]),float(args[2]))), Vector((0,0)), (objectSprite.frameWidth,objectSprite.frameHeight), 100,objectSprite, int(args[3])))
        for line in file:
            args = line.split(",")
            objectSprite = Sprite(args[0])
            if(args[1]== "mid"):
                #have to convert to string to store and then reconvert later
                #bit dodgy but prevents code duplication
                args[1] = str(self.background.foregroundPos.x)

            self.objects.append(GameObject(Vector((float(args[1]),float(args[2]))), Vector((0,0)), (objectSprite.frameWidth,objectSprite.frameHeight), 100,objectSprite))
    def setPlayer(self,player):
        self.player = player

    #draws all the entities
    def draw(self, canvas):
        self.update()
        self.inter.text.display(canvas)
        self.background.update(canvas, self.player)
        self.player.draw(canvas, "Green")
        for proj in self.player.projectiles:
            proj.draw(canvas, "Blue")
        for fireball in self.player.fireballs:
            fireball.draw(canvas, "Blue")
        for enemy in self.enemies:
            enemy.draw(canvas, "Red")
            for proj in enemy.projectiles:
                proj.draw(canvas, "Blue")
        for objectOnScreen in self.objects:
            objectOnScreen.draw(canvas, "Purple")
        self.displayBar.drawDisplayBar(canvas)

    #checks for input and collisions
    def update(self):
        self.displayBar.updateBar(self.player.health, self.player.maxUnlockedWeapon, 3 - self.player.numberOfDeaths)
        self.inter.checkProjectileCollision(self.enemies,self.player)
        self.inter.checkObjectCollision(self.objects, self.player)
        for enemy in self.enemies:
            self.inter.checkObjectCollision(self.objects,enemy)
        self.inter.checkKeyboard()
        #update the location of all of the elements if the canvas is moving
        if (self.background.foregroundVel.x !=0):
            self.player.position.add(self.background.foregroundVel)
            #fix everything in place
            for proj in self.player.projectiles:
                proj.position.add(self.background.foregroundVel)
            for enemy in self.enemies:
                enemy.position.add(self.background.foregroundVel)
            for currentObject in self.objects:
                currentObject.position.add(self.background.foregroundVel)
        #has to be in a separate loop because it uses a copy of list
        for proj in self.player.projectiles[:]:
            if proj.boundingBox.right<0:
                self.player.projectiles.remove(proj)
        for enemy in self.enemies[:]:
            if enemy.boundingBox.right<0:
                self.enemies.remove(enemy)
        for currentObject in self.objects[:]:
            if currentObject.boundingBox.right<0:
                self.objects.remove(currentObject)

    #returns the player so they can be passed on to next level
    def returnPlayer(self):
        return self.player

    #returns true if level is over
    def levelComplete(self):
        #check if the character is in the last x number of pixels of the screen
        return(not self.background.isStillRunning()) and (self.player.position.x > GV.CANVAS_WIDTH - 70) and (len(self.enemies) ==0)
