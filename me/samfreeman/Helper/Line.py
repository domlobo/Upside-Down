from me.samfreeman.Helper.Vector import Vector


class Line:
    def __init__(self, pointA, pointB, thickness):
        self.pointA = pointA
        self.pointB = pointB
        self.thickness = thickness

    def draw(self, canvas):
        canvas.draw_line(self.pointA.getP(), self.pointB.getP(), self.thickness, "Blue")
