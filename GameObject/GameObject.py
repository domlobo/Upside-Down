from Helper.Rectangle import Rectangle


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

        # Boolean
        self.remove = False

    def changeHealth(self, health):
        self.health += health

    def setHealth(self, amount):
        self.health = amount

    def update(self):
        self.position.add(self.velocity)
        self.boundingBox.updateBox(self.position, self.dimensions[0], self.dimensions[1])
        if self.health <= 0: self.remove = True

        #either in bounds, or right bound moving left or left bound moving right
        self.position.add(self.velocity)
        self.boundingBox.updateBox(self.position, self.dimensions[0], self.dimensions[1])
        # Overwrite and add anything else

    def draw(self, canvas, colour):
        self.update()
        # Bounding box for testing
        self.boundingBox.draw(canvas, colour)
