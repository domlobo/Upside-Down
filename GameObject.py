from Vector import Vector
from Rectangle import Rectangle
import GV


class GameObject:
    def __init__(self, position, velocity, dimensions, health, sprite = ""):
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

        # 'Bounding Box'
        self.boundingBox = Rectangle(self.position, self.dimensions[0], self.dimensions[1])

    def changeHealth(self, health):
        self.health += health

    def setHealth(self, amount):
        self.health = amount

    def update(self):
        #either in bounds, or right bound moving left or left bound moving right
        if((self.position.x < GV.CANVAS_WIDTH)and (self.position.x > 0)) or ((self.position.x>=GV.CANVAS_WIDTH ) and (self.velocity.x <0)) or ((self.position.x <=0)and (self.velocity.x>0)):
            self.position.add(self.velocity)
            self.boundingBox.updateBox(self.position)
        # Overwrite and add anything else

    def draw(self, canvas, colour):
        self.update()
        # Bounding box for testing
        self.boundingBox.draw(canvas, colour)
