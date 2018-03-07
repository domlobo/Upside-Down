# Import
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite


class BasicEnemy(GameObject):
    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite("")):
        dims = [30,60]
        if runLeft.loaded:
            dims = [runLeft.frameWidth, runLeft.frameHeight]

        GameObject.__init__(self, position, Vector((0, 0)),dims , health)
        self.player = player
        self.direction = 0

        self.maxVel = [3, 3]

        # 'AI'
        self.largeSearch = Rectangle(self.position, 250, 250)
        self.smallSearch = Rectangle(self.position, 150, 150)
        self.movementRectangle = Rectangle(self.position, 200, 200)
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

        if dl.x < 0:
            self.sprite = self.runningLeft
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else: self.velocity.x += dl.x
        else:
            self.sprite = self.runningRight
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += dl.x
        if self.sprite.loaded:
            self.sprite.animate(5)

    def move(self):
        speed = 0.9
        if self.position.x >= self.movementRectangle.right:
            self.velocity *= -1
        if self.position.x <= self.movementRectangle.left:
            self.velocity *= -1

        if self.velocity.x < 0:
            self.sprite = self.runningLeft
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else:
                self.velocity.x -= (speed)
        else:
            self.sprite = self.runningRight
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += (speed)
        if self.sprite.loaded:
            self.sprite.animate(10)
    def update(self):
        GameObject.update(self)
        self.findPlayer()

    def draw(self, canvas, colour):
        print(self.sprite)
        GameObject.draw(self, canvas, colour)
        self.largeSearch.draw(canvas, "White")
