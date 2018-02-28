from Vector import Vector

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
        self.left = self.position.x -(self.dimensions[0] / 2)
        self.right = self.position.x + (self.dimensions[0] / 2)
        self.top = self.position.y - (self.dimensions[1] / 2)
        self.bottom = self.position.y + (self.dimensions[1] / 2)

    def changeHealth(self, health):
        self.health += health

    def setHealth(self, amount):
        self.health = amount

    def updateBox(self):
        self.left = self.position.x - (self.dimensions[0] / 2)
        self.right = self.position.x + (self.dimensions[0] / 2)
        self.top = self.position.y -(self.dimensions[1] / 2)
        self.bottom = self.position.y + (self.dimensions[1] / 2)

    def update(self):
        self.position.add(self.velocity)
        self.updateBox()
        # Overwrite and add anything else

    def draw(self, canvas):
        self.update()
        # Bounding box for testing
        canvas.draw_polygon([(self.left, self.top), (self.right, self.top), (self.right, self.bottom), (self.left, self.bottom)], 1, "Red")

