#imports
from GameObject import GameObject
from Vector import Vector
from Rectangle import Rectangle

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
        self.movementRectangle.updateBox(self.position)


    def findPlayer(self):
        # Update the search rectangles
        self.largeSearch.updateBox(self.position)
        self.smallSearch.updateBox(self.position)

        # Checks first in large rectangle
        if self.largeSearch.contains(self.player.position):
            # Inside large
            self.resetMovement()
            print("Player found in largest box")
            self.moveToPlayer()
            if self.smallSearch.overlaps(self.player.boundingBox):
                print("Player found in small circle")
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
            else: self.velocity.add(dl)
        else:
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.add(dl)

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

        print(self.velocity.x)

    def update(self):
        GameObject.update(self)
        self.findPlayer()
