
from Helper.Rectangle import Rectangle
import GameControl.GV as GV
from Helper.Vector import Vector

class DisplayBar():

    def __init__(self, levelName, health, currentWeapon, topSpace = 55):
        self.levelName = levelName
        self.health = health
        self.topSpace = topSpace
        self.boundingBox = Rectangle(Vector((GV.CANVAS_WIDTH / 2, self.topSpace / 2)), GV.CANVAS_WIDTH, self.topSpace)
        self.currentWeapon = currentWeapon

        edge = self.topSpace * 0.8
        self.weaponDisplayBoundingBox = Rectangle(Vector((GV.CANVAS_WIDTH / 2, self.topSpace / 2)), edge, edge)

    def updateBar(self, health, currentWeapon):
        self.health = health

        # Going to need some method that selects the weapon image/sprite based on the currentweapon
        self.currentWeapon = currentWeapon

    def drawDisplayBar(self, canvas):
        # Text is lower left point
        canvas.draw_text(self.levelName, [20, self.boundingBox.position.y], 20, "White")
        canvas.draw_text(str(self.health), [self.boundingBox.right - 80, self.boundingBox.position.y], 20, "White")
        self.weaponDisplayBoundingBox.draw(canvas, "Blue")