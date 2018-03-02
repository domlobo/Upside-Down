#imports
from GameObject.GameObject import GameObject
from Helper.Rectangle import Rectangle
from Helper.Vector import Vector


class BasicEnemy(GameObject):
    def __init__(self, position, health, player):
        GameObject.__init__(self, position, Vector((0, 0)), [30, 60], health)
        self.player = player
        self.direction = 0

        self.maxVel = [3, 3]

        # 'AI'
        self.largeSearch = Rectangle(self.position, 250, 250)
        self.smallSearch = Rectangle(self.position, 150, 150)
        self.movementRectangle = Rectangle(self.position, 200, 200)
        # Will uncomment when I get the search rectangles working

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
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else: self.velocity.x += dl.x
        else:
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += dl.x

    def move(self):
        speed = 0.9
        if self.position.x >= self.movementRectangle.right:
            self.velocity *= -1
        if self.position.x <= self.movementRectangle.left:
            self.velocity *= -1

        if self.velocity.x < 0:
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else:
                self.velocity.x -= (speed)
        else:
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += (speed)

    def update(self):
        GameObject.update(self)
        self.findPlayer()

    def draw(self, canvas, colour):
        GameObject.draw(self, canvas, colour)
        self.largeSearch.draw(canvas, "White")
