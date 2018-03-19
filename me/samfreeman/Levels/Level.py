try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.GameObject.StaticEnemy import StaticEnemy
from me.samfreeman.GameObject.ProjectileEnemy import ProjectileEnemy
from me.samfreeman.GameObject.ProjBossCharacter import ProjBossCharacter
from me.samfreeman.GameObject.MarioBossCharacter import MarioBossCharacter
from me.samfreeman.Helper.Display import DisplayBar
from me.samfreeman.Helper.Background import Background
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite

class Level:

    def __init__(self, backgroundURL, foregroundURL, cloudsURL, player,inter, name):
        self.background = Background(backgroundURL, foregroundURL, cloudsURL)
        self.enemies = []
        self.objects = []
        self.collectibles = []
        self.player = player
        self.inter = inter
        self.displayBar = DisplayBar(name, self.player.health)
        self.dropLocation = Vector()

    #load the enemies into the class
    def loadLevelSpecifics(self, fileLocation):
        file = open(fileLocation, "r")
        #load all the text to be displayed
        for line in file:
            #if this section is over, break
            if line == "Enemies\n":
                 break
            #args[0] is speach, args[1] is the speaker
            args = line.split("|")
            self.inter.text.addLine(args[0],int(args[1]))

        self.inter.text.nextText()
        #load the enemies
        for line in file:
            #if this section is over, break
            if line == "Walls\n":
                break
            #arg[0] is x pos, arg[1] is y pos, arg[2] is health, args[3] and arg[5] are left and right sprites with args[4] and args[6] being the number of colums, args[7] denotes the type of enemy
            args = line.split(",")
            runLeft = Sprite(args[3], 1,int(args[4]), True)
            if(args[7] == "d\n"):
                runRight= Sprite(args[5], 1,int(args[6]), True)
                self.enemies.append(BasicEnemy(Vector((int(args[0]), int(args[1]))),int(args[2]),self.player, runLeft, runRight))
            elif(args[7] == "s\n"):
                #args[5] and [6] are left blank
                self.enemies.append(StaticEnemy(Vector((int(args[0]), int(args[1]))),int(args[2]),self.player, runLeft))
            elif(args[7] == "r\n"):
                runRight= Sprite(args[5], 1,int(args[6]), True)
                leftShoot = Sprite(args[8],1, int(args[9]), True)
                rightShoot = Sprite(args[10],1, int(args[11]), True)
                self.enemies.append(ProjectileEnemy(Vector((int(args[0]), int(args[1]))),int(args[2]),self.player, runLeft, runRight, leftShoot, rightShoot))
            elif(args[7] == "bl"):
                runRight= Sprite(args[5], 1,int(args[6]), True)
                weapon = Sprite(args[8])
                attackLeft = Sprite(args[9],1,int(args[10]),True)
                attackRight = Sprite(args[11],1,int(args[12]),True)
                projLeft = Sprite(args[13])
                projRight = Sprite(args[14])
                self.enemies.append(ProjBossCharacter(Vector((int(args[0]), int(args[1]))),int(args[2]),self.player, runLeft, runRight,weapon,attackLeft,attackRight,projLeft,projRight))
            elif(args[7] == "bm\n"):
                runRight= Sprite(args[5], 1,int(args[6]), True)
                self.enemies.append(MarioBossCharacter(Vector((int(args[0]), int(args[1]))),int(args[2]),self.player, runLeft, runRight))
        #load all the objects
        for line in file:
            if line == "Floor\n":
                break
            #arg[0] is image path, arg[1] is x pos, arg[2] is y pos, args[3] is notCollibable as an int
            args = line.split(",")
            objectSprite = Sprite(args[0])
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
        for proj in self.player.projectiles:
            proj.draw(canvas, "Blue")
        for fireball in self.player.fireballs:
            fireball.draw(canvas, "Blue")
        for enemy in self.enemies:

            enemy.draw(canvas, "Red")
            for proj in enemy.projectiles:
                proj.draw(canvas, "Blue")
            if hasattr(enemy, 'fireballs'):
                for fball in enemy.fireballs:
                    fball.draw(canvas,"Blue")
        for objectOnScreen in self.objects:
            objectOnScreen.draw(canvas, "Purple")
        self.displayBar.drawDisplayBar(canvas)
        for collectible in self.collectibles: collectible.draw(canvas)
        self.player.draw(canvas, "Green")

    #checks for input and collisions
    def update(self):
        self.displayBar.updateBar(self.player.health, self.player.maxUnlockedWeapon, 3 - self.player.numberOfDeaths, self.player.collectedCoins)
        self.inter.checkProjectileCollision(self.enemies,self.player)
        self.inter.checkObjectCollision(self.objects, self.player)
        self.inter.checkCollectibleCollision(self.collectibles, self.player)
        for enemy in self.enemies:
            self.inter.checkObjectCollision(self.objects,enemy)
            if hasattr(enemy, 'fireballs'):
                for fball in enemy.fireballs:
                    self.inter.checkObjectCollision(self.objects, fball)
            if enemy.health <= 0:
                if enemy.boss:
                    self.collectibles.append(enemy.dropWeapon())
                self.collectibles.append(enemy.dropCoin(100, 1))

        self.inter.checkKeyboard()

        for collectible in self.collectibles[:]:
            if collectible.position.x <0:
                collectible.setRemove()
                continue
            collectible.update(self.background.foregroundVel.copy())
            if collectible.remove: self.collectibles.remove(collectible)

        #update the location of all of the elements if the canvas is moving
        if (self.background.foregroundVel.x <0):
            #variable to keep relative positions the same when background moves
            movementVariable =1.25*self.background.foregroundVel
            #stopping right hand pushing
            self.player.position.add(movementVariable)
            #fix everything in place
            for proj in self.player.projectiles:
                proj.position.add(movementVariable)
            for enemy in self.enemies:
                enemy.position.add(self.background.foregroundVel)
                enemy.resetMovement()
            for currentObject in self.objects:
                currentObject.position.add(self.background.foregroundVel)
        #has to be in a separate loop because it uses a copy of list
        for proj in self.player.projectiles[:]:
            if proj.boundingBox.right<0:
                self.player.projectiles.remove(proj)
        for enemy in self.enemies[:]:
            if enemy.boundingBox.right<0 or (enemy.boundingBox.left>=GV.CANVAS_WIDTH and not(self.background.isStillRunning())) or enemy.position.y >= GV.CANVAS_HEIGHT:
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
