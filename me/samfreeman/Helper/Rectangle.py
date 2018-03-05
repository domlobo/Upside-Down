

class Rectangle():
    def __init__(self, position, width, height):
        # Vector, int, int
        # Assumes pos is in the centre of the object
        self.position = position
        self.width = width
        self.height = height

        self.left = self.position.x - (self.width / 2)
        self.right = self.position.x + (self.width / 2)
        self.top = self.position.y - (self.height / 2)
        self.bottom = self.position.y + (self.height / 2)

        # self.topLeft = Vector((self.left, self.top))
        # self.bottomRight = Vector((self.right, self.bottom))

    def updateBox(self, position, width, height):
        self.position = position

        self.width = width
        self.height = height

        self.left = self.position.x - (self.width / 2)
        self.right = self.position.x + (self.width / 2)
        self.top = self.position.y - (self.height / 2)
        self.bottom = self.position.y + (self.height / 2)

    def overlaps(self, other):
        # Rectangle
        # Checks if two rectangles are overlapping (intersecting)

        # return ((self.topLeft.x > other.bottomRight.x) or
        #         (self.bottomRight.x < other.topLeft.x) or
        #         (self.topLeft.y  > other.bottomRight.y) or
        #         (self.bottomRight.y < other.topLeft.y))

        return (self.left < other.right and
                self.right > other.left and
                self.top < other.bottom and
                self.bottom > other.top)

    def contains(self, point):
        # Vector
        return (self.right >= point.x >= self.left and
                self.bottom >= point.y >= self.top)

    def draw(self, canvas, colour, background=""):
        if background == "":
            canvas.draw_polygon([(self.left, self.top), (self.right, self.top), (self.right, self.bottom), (self.left, self.bottom)], 1, colour)
        else:
            canvas.draw_polygon([(self.left, self.top), (self.right, self.top), (self.right, self.bottom), (self.left, self.bottom)], 1, colour, background)
