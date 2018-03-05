
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Vector import Vector

class DisplayBar():

    def __init__(self, levelName, health, currentWeapon, topSpace = 55):
        self.levelName = levelName
        self.health = health
        self.topSpace = topSpace
        self.boundingBox = Rectangle(Vector((GV.CANVAS_WIDTH / 2, self.topSpace / 2)), GV.CANVAS_WIDTH, self.topSpace)

        # TODO: Assuming there is some aspect of the sprite that has an array of the sprite sheet
        self.healthSpriteSheet = []
        self.currentSprite = 0

        # Hold the weapon sprites in an array
        self.currentWeapon = currentWeapon
        self.weaponSprites = []

        edge = self.topSpace * 0.8
        self.weaponDisplayBoundingBox = Rectangle(Vector((GV.CANVAS_WIDTH / 2, self.topSpace / 2)), edge, edge)

    def updateBar(self, health, currentWeapon):
        self.health = health
        # There 10 hearts as part of the sheet
        # Use [0] for 0-10 health, [1] for 11-20.. etc.
        self.currentSprite = self.health // 10

        self.currentWeapon = currentWeapon

    def drawDisplayBar(self, canvas):
        # Text is lower left point
        canvas.draw_text(self.levelName, [20, self.boundingBox.position.y], 20, "White")
        canvas.draw_text(str(self.health), [self.boundingBox.right - 80, self.boundingBox.position.y], 20, "White")
        self.weaponDisplayBoundingBox.draw(canvas, "Blue")

        # TODO: Add the method for the drawing of the health.. hopefully would be something like healthSpriteSheet[currentSprite]
        # TODO: DRAW THE WEAPON BY self.weaponSprites[currentWeapon].draw or something