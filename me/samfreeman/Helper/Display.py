
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite
import os.path

class DisplayBar:

    def __init__(self, levelName, health, topSpace = 55):
        self.levelName = levelName
        self.health = health
        self.topSpace = topSpace
        self.boundingBox = Rectangle(Vector((GV.CANVAS_WIDTH / 2, self.topSpace / 2)), GV.CANVAS_WIDTH, self.topSpace)
        self.healthSpriteSheet = Sprite("images/interactive-sprites/display/health.png", 1, 10)
        self.currentSprite = 0
        self.lives = 3

        self.weaponSprites = Sprite("images/interactive-sprites/display/weapons.png", 1, 4)

        self.unlockedWeapons = 4 # TODO: GET THIS FROM SOMEWHERE
        self.allWeapons = [self.weaponSprites.spriteFromIndex([i, 0]) for i in range(0, self.unlockedWeapons)]

        self.edge = self.topSpace * 0.8

        self.adjustment = 1 if self.unlockedWeapons == 1 else 2

        self.containerRect = Rectangle(Vector((GV.CANVAS_WIDTH / 2, self.topSpace / 2)), (self.unlockedWeapons - self.adjustment) * (self.edge) * 1.5, self.edge)
        self.weaponDisplayLeft = (self.containerRect.position.x - self.containerRect.width / 2)

    def updateBar(self, health, maxWeapon, lives):
        self.health = health
        # There 10 hearts as part of the sheet
        # Use [0] for 0-10 health, [1] for 11-20.. etc.
        self.currentSprite = self.health // 10 - 1
        self.healthSpriteSheet.setIndex([self.currentSprite, 0])
        self.lives = lives
        self.unlockedWeapons = maxWeapon + 1

        self.containerRect = Rectangle(Vector((GV.CANVAS_WIDTH / 2, self.topSpace / 2)), (self.unlockedWeapons - self.adjustment) * (self.edge) * 1.5, self.edge)
        self.weaponDisplayLeft = (self.containerRect.position.x - self.containerRect.width / 2)

    def drawDisplayBar(self, canvas):
        # Text is lower left point
        canvas.draw_text(self.levelName, [20, self.boundingBox.position.y], 20, "White")
        healthPosX = self.boundingBox.right - self.topSpace + 10
        self.healthSpriteSheet.draw(Vector((healthPosX, self.topSpace / 2)), canvas, self.topSpace - 10, self.topSpace - 10)
        canvas.draw_text(str(self.lives), [(healthPosX - (self.topSpace - 10) / 2) + 18, (self.topSpace) - 15], 25, "White", "sans-serif")

        for i in range(0, self.unlockedWeapons):
            offset = i
            spacing = self.edge * 2

            if self.unlockedWeapons > 1:
                if i == 0: continue
                else: offset = i - 1

            self.allWeapons[i].draw(Vector((self.weaponDisplayLeft + offset * spacing, self.containerRect.position.y)), canvas, self.edge, self.edge)
