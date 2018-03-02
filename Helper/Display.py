
from Helper.Rectangle import Rectangle
import GameControl.GV as GV
from Helper.Vector import Vector

class DisplayBar():

    def __init__(self, levelName, health, topSpace = 55):
        self.levelName = levelName
        self.health = health
        self.topSpace = topSpace
        self.boundingBox = Rectangle(Vector((GV.CANVAS_WIDTH / 2, self.topSpace / 2)), GV.CANVAS_WIDTH, self.topSpace)

    def updateBar(self, health):
        self.health = health

    def drawDisplayBar(self, canvas):
        # Text is lower left point
        canvas.draw_text(self.levelName, [20, self.boundingBox.position.y], 20, "White")
        canvas.draw_text(str(self.health), [self.boundingBox.right - 80, self.boundingBox.position.y], 20, "White")