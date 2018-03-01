from Vector import Vector
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

    def overlaps(self, other):
        # Rectangle
        # Checks if two rectangles are overlapping (intersecting)

        # return ((self.topLeft.x > other.bottomRight.x) or
        #         (self.bottomRight.x < other.topLeft.x) or
        #         (self.topLeft.y  > other.bottomRight.y) or
        #         (self.bottomRight.y < other.topLeft.y))

        return (self.left > other.right or
                self.right < other.left or
                self.top > other.bottom or
                self.bottom < other.top)

    def contains(self, point):
        # Vector
        return (self.right >= point.x >= self.left and
                self.bottom >= point.y >= self.top)


