# Import
from me.samfreeman.GameObject.Coin import Coin
from me.samfreeman.GameObject.WeaponPickUp import WeaponPickUp
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite
import me.samfreeman.GameControl.GV as GV

class BasicEnemy(GameObject):

    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite(""), boss=False, weapon=Sprite("")):
        dims = [30,60]
        if runLeft.hasPath:
            dims = [runLeft.frameWidth, runLeft.frameHeight]
        GameObject.__init__(self, position, Vector((0.2, 0)),dims , health)
        self.player = player
        self.direction = GV.RIGHT
        self.damage = 0.5
        self.projectiles = []

        self.maxVel = [1, 1]
        self.lastSwitch = "Null"

        # 'AI'
        self.largeSearch = Rectangle(self.position, 600, 400)
        self.smallSearch = Rectangle(self.position, 150, 150)
        self.movementRectangle = Rectangle(self.position, 200, 200)
        self.sprite = runRight
        self.runningLeft = runLeft
        self.runningRight = runRight
        self.gravity =1
        self.boss = boss

        self.weapon = weapon

    def resetMovement(self):
        # Used to make a new movement box when the user moves out of it
        self.movementRectangle.updateBox(self.position, 200, 200)

    def findPlayer(self):
        # Update the search rectangles
        self.largeSearch.updateBox(self.position, 600, 250)
        self.smallSearch.updateBox(self.position, 150, 150)

        # Checks first in large rectangle
        if self.largeSearch.overlaps(self.player.boundingBox):
            # Inside large
            self.resetMovement()
            self.moveToPlayer()
            if self.smallSearch.overlaps(self.player.boundingBox):
                pass
        else:
            self.move()

    def moveToPlayer(self):
        currentPPos = self.player.position
        dx = currentPPos.x - self.position.x
        dy = currentPPos.y - self.position.y

        dl = Vector((dx, dy)).normalize()

        self.checkOutSideMovementBox()

        if not(self.canMoveLeft):
            self.sprite = self.runningRight
        elif not(self.canMoveRight):
            self.sprite = self.runningLeft

        if dl.x < 0 and self.canMoveLeft:
            self.sprite = self.runningLeft
            self.direction = GV.LEFT
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else: self.velocity.x += dl.x
            self.lastSwitch = "Null"
        elif dl.x >0 and self.canMoveRight:
            self.direction = GV.RIGHT
            self.sprite = self.runningRight
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += dl.x
            self.lastSwitch = "Null"
        else: #if self.lastSwitch != "Switched":

            self.direction = (self.direction+1) %2
            self.velocity *=  -1
            if self.direction == GV.LEFT:
                self.sprite = self.runningLeft
            else:
                self.sprite = self.runningRight
            self.lastSwitch = "Switched"
        if self.sprite.hasPath:
            self.sprite.startAnimation(5)

            if self.canMoveDown:
                self.velocity.y +=self.gravity
                self.velocity.x = 0

    def move(self):
        # if self.position.x >GV.CANVAS_WIDTH+self.sprite.frameWidth/2:
        #     return
        speed = 0.9
        #switch direction if you can't move
        self.checkOutSideMovementBox()

        if (self.velocity.x < 0) and self.canMoveLeft:
            self.sprite = self.runningLeft
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else:
                self.velocity.x -= (speed)
        if (self.velocity.x >= 0) and self.canMoveRight:
            self.sprite = self.runningRight
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += (speed)
        if self.sprite.hasPath:
            self.sprite.startAnimation(10)
        if self.canMoveDown:
            self.velocity.y +=self.gravity
            self.velocity.x = 0

    def dropCoin(self, size, cost):
        return Coin(self.position, size, cost)

    def dropWeapon(self):
        return WeaponPickUp(Vector((self.position.x, self.position.y + self.dimensions[1] / 2-30)), self.player, self.weapon) # 30 is half the height of the image being drawn

    def checkOutSideMovementBox(self):
        if(self.position.x >= self.movementRectangle.right) or (self.position.x <= self.movementRectangle.left):
            self.velocity.x*= -1
            self.lastSwitch = "Null"
            self.direction = (self.direction+1) %2
        elif (not(self.canMoveRight) and self.lastSwitch != "Right"):
            self.velocity.x*= -1
            self.lastSwitch = "Right"
            self.direction = GV.LEFT
        elif(not(self.canMoveLeft) and self.lastSwitch != "Left"):
            self.velocity.x*= -1
            self.lastSwitch = "Left"
            self.direction = GV.RIGHT

    def update(self):
        if GV.allow_update:
            GameObject.update(self)
            self.findPlayer()
        # Projectiles
        for proj in self.projectiles[:]:
            proj.update()
            if proj.position.x <=0  or proj.position.x >= GV.CANVAS_WIDTH:
                proj.remove = True
            if proj.remove: self.projectiles.remove(proj)

    def draw(self, canvas, colour):
        GameObject.draw(self, canvas, colour)
        self.largeSearch.draw(canvas, "White")
