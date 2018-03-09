from me.samfreeman.Helper.Vector import Vector


class Line:
    def __init__(self, pointA, pointB, thickness):
        self.pointA = pointA
        self.pointB = pointB
        self.thickness = thickness

    def draw(self, canvas):
        canvas.draw_line(self.pointA.getP(), self.pointB.getP(), self.thickness, "Blue")

    #check if the line endPoint is inside a Rectangle
    def overlaps(self, other):
        return(self.pointB.x <= other.right
                and self.pointB.x >= other.left
                and self.pointB.y <= other.bottom
                and self.pointB.y >= other.top)
