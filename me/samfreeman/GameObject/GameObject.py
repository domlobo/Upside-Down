from me.samfreeman.GameControl import GV
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Clock import Clock

class GameObject:
    def __init__(self, position, velocity, dimensions, health, sprite=Sprite(""),notCollidable=0):
        # Vectors
        self.position = position
        self.velocity = velocity

        # Tuple
        #[x, y]
        self.dimensions = dimensions

        # Sprite
        self.sprite = sprite

        # Integers
        self.health = health


        self.boundingBox = Rectangle(self.position, self.dimensions[0], self.dimensions[1])

        # Boolean
        self.remove = False

        #fake boolean
        self.notCollidable = notCollidable

        #can move booleans
        self.canMoveLeft = True
        self.canMoveRight = True
        self.canMoveUp = True
        self.canMoveDown = True

        self.hasJumped = False
        self.currentGround = self.position.y + self.dimensions[1]/2

        self.checkPosition = True

    def setRemove(self):
        self.remove = True

    def updateSprite(self, sprite):
        self.sprite = sprite

    def changeHealth(self, health):
        self.health += health

    def setHealth(self, amount):
        self.health = amount

    def update(self, ground=0):
        #check haven't fallen into ground
        if self.checkPosition and self.velocity.y ==0 and self.position.y+self.dimensions[1]/2 > self.currentGround :
            self.position.y = self.currentGround -self.dimensions[1]/2
            self.checkPosition = False
        self.position.add(self.velocity)
        self.boundingBox.updateBox(self.position, self.dimensions[0], self.dimensions[1])
        if self.health <= 0: self.remove = True

        #either in bounds, or right bound moving left or left bound moving right
        self.position.add(self.velocity)
        self.boundingBox.updateBox(self.position, self.dimensions[0], self.dimensions[1])
        # Overwrite and add anything else

    def draw(self, canvas, colour, position=Vector((-1,-1)), width=0):

        width = self.dimensions[0] if width == 0 else width
        if position.x == -1 and position.y == -1:
            position = self.position
        self.update()
        if self.sprite.hasPath:
            self.sprite.draw(position, canvas, width, self.dimensions[1])
        # Bounding box for testing
        self.boundingBox.draw(canvas, colour)
