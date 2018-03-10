# Import
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite
import me.samfreeman.GameControl.GV as GV


class BasicEnemy(GameObject):
    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite("")):
        dims = [30,60]
        print(position)
        if runLeft.loaded:
            dims = [runLeft.frameWidth, runLeft.frameHeight]
        GameObject.__init__(self, position, Vector((0, 0)),dims , health)
        self.player = player
        self.direction = 0
        self.damage = 0.5
        self.projectiles = []

        self.maxVel = [3, 3]
        self.lastSwitch = "Null"

        # 'AI'
        self.largeSearch = Rectangle(self.position, 250, 250)
        self.smallSearch = Rectangle(self.position, 150, 150)
        self.movementRectangle = Rectangle(self.position, 200, 200)
        self.sprite = runRight
        self.runningLeft = runLeft
        self.runningRight = runRight

    def resetMovement(self):
        # Used to make a new movement box when the user moves out of it
        self.movementRectangle.updateBox(self.position, 200, 200)

    def findPlayer(self):
        # Update the search rectangles
        self.largeSearch.updateBox(self.position, 250, 250)
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

        if dl.x < 0 and self.canMoveLeft:
            self.sprite = self.runningLeft
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else: self.velocity.x += dl.x
            self.lastSwitch = "Null"
        elif dl.x >=0 and self.canMoveRight:
            self.sprite = self.runningRight
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += dl.x
            self.lastSwitch = "Null"
        elif self.lastSwitch != "Switched":
            self.velocity *=  -1
            self.lastSwitch = "Switched"
        if self.sprite.loaded:
            self.sprite.animate(5)

    def move(self):
        speed = 0.9
        #switch direction if you can't move
        if(self.position.x >= self.movementRectangle.right) or (self.position.x <= self.movementRectangle.left):
            self.velocity*= -1
            self.lastSwitch = "Null"
        elif (not(self.canMoveRight) and self.lastSwitch != "Right"):
            self.velocity *= -1
            self.lastSwitch = "Right"
        elif(not(self.canMoveLeft) and self.lastSwitch != "Left"):
            self.velocity *= -1
            self.lastSwitch = "Left"

        if (self.velocity.x < 0) and self.canMoveLeft:
            self.sprite = self.runningLeft
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else:
                self.velocity.x -= (speed)
        elif (self.velocity.x>=0) and self.canMoveRight:
            self.sprite = self.runningRight
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += (speed)
        else:
            self.velocity.x = 0
        if self.sprite.loaded:
            self.sprite.animate(10)
    def update(self):
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
