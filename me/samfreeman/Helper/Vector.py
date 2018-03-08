import math

# The Vector class
class Vector:
    # Initialiser
    def __init__(self, p=(0, 0)):
        self.x = p[0]
        self.y = p[1]

    # Returns a string representation of the vector
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Tests the equality of this vector and another
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Tests the inequality of this vector and another
    def __ne__(self, other):
        return not self.__eq__(other)

    # Returns a tuple with the point corresponding to the vector
    def getP(self):
        return (self.x, self.y)

    # Returns a copy of the vector
    def copy(self):
        v = Vector()
        v.x = self.x
        v.y = self.y
        return v

    # Adds another vector to this vector
    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        return self.copy().add(other);

    # Negates the vector (makes it point in the opposite direction)
    def negate(self):
        return self.multiply(-1)

    def __neg__(self):
        return self.copy().negate()

    # Subtracts another vector from this vector
    def sub(self, other):
        return self.add(-other)

    def __sub__(self, other):
        return self.copy().sub(other)

    # multiplyiplies the vector by a scalar
    def multiply(self, k):
        self.x *= k
        self.y *= k
        return self

    def __mul__(self, k):
        return self.copy().multiply(k)

    def __rmul__(self, k):
        return self.copy().multiply(k)

    # Divides the vector by a scalar
    def divide(self, k):
        return self.multiply(1 / k)

    def __truediv__(self, k):
        return self.copy().divide(k)

    # Normalizes the vector
    def normalize(self):
        return self.divide(self.length())

    # Returns a normalized version of the vector
    def getNormalized(self):
        return self.copy().normalize()

    # Returns the dot product of this vector with another one
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Returns the length of the vector
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Returns the squared length of the vector
    def lengthSquared(self):
        return self.x ** 2 + self.y ** 2

    # Reflect this vector on a normal
    def reflect(self, normal):
        n = normal.copy()
        n.multiply(2 * self.dot(normal))
        self.sub(n)
        return self

    # Returns the angle between this vector and another one
    def angle(self, other):
        return math.acos(self.dot(other) / (self.length() * other.length()))

    # Rotates the vector 90 degrees anticlockwise
    def rotateAnti(self):
        self.x, self.y = -self.y, self.x
        return self

    # Rotates the vector according to an angle theta given in radians
    def rotateRad(self, theta):
        rx = self.x * math.cos(theta) - self.y * math.sin(theta)
        ry = self.x * math.sin(theta) + self.y * math.cos(theta)
        self.x, self.y = rx, ry
        return self

    # Rotates the vector according to an angle theta given in degrees
    def rotate(self, theta):
        thetaRad = theta / 180 * math.pi
        return self.rotateRad(thetaRad)