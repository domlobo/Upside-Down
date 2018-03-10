# Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from me.samfreeman.Helper.Clock import Clock
import os.path

class Sprite:

    def __init__(self, assetPath, isSpriteSheet = False, rows=1, cols=1):
        if assetPath != "":
            self.image = simplegui._load_local_image(assetPath)
            self.loaded = True
            print(assetPath)
        else: self.loaded = False
        self.isSpriteSheet = isSpriteSheet
        self.rows = rows
        self.cols = cols
        self.name = assetPath
        self.startOffset = (0,0)
        self.animationLength = self.cols

        # Display Information
        if self.loaded:
            self.frameWidth = self.image.get_width() / self.cols
            self.frameHeight = self.image.get_height() / self.rows
            self.frameIndex = [0, 0]
            self.frameCentre = (self.frameWidth / 2, self.frameHeight / 2)

        self.animationClock = Clock()

        self.isAnimating = 0
        self.needTick = False


    def animate(self, frameDuration, start=[0,0], length = 0):
        # Will animate while it is being called (such as moving a player)
        self.startOffset = start
        if length != 0: self.animationLength = length
        self.needTick = True
        if self.animationClock.transition(frameDuration):
            self.frameIndex[0] = self.startOffset[0] + (self.frameIndex[0] + 1) % (self.startOffset[0] // self.cols + self.animationLength)
            self.frameIndex[1] = self.startOffset[1]
            # if self.frameIndex[0] == 0:
            #     self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows

    def animateFull(self, frameDuration):
        # Will animate without moving (go through entire sprite sheet)
        self.needTick = True
        #print("Time: " + str(self.animationClock.time) + " FI: " + str(self.frameIndex))
        if self.animationClock.transition(frameDuration):
            self.frameIndex[1] = self.startOffset[1]
            self.frameIndex[0] = self.startOffset[0] + (self.frameIndex[0] + 1) % (self.startOffset[0] // self.cols + self.animationLength)

            # print(str(self.startOffset[1]) + " " + str(self.frameIndex[0]))
            if self.frameIndex[0] == self.startOffset[0]:
                # self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows
                self.isAnimating = 0

    def setAnimating(self, frameDuration, start, length, reset):
        self.isAnimating = frameDuration
        self.startOffset = start
        self.animationLength = length
        if reset: self.animationClock.time = 0

    def stopAnimating(self):
        self.needTick = False

    def setIndex(self, index):
        self.frameIndex = index

    def draw(self, position, canvas, width=0, height=0):
        # Target width and height
        # If no width or height is specified, it will display the full size of the image
        d_width = self.frameWidth # Destination width
        d_height = self.frameHeight  # Destination height

        if width > 0: d_width = width
        if height > 0: d_height = height

        if self.needTick:
            self.animationClock.tick()
        else:
            self.animationClock.time = 0

        if self.isAnimating > 0:
            self.animateFull(self.isAnimating)

        canvas.draw_image(
            self.image,
            (self.frameWidth*self.frameIndex[0]+self.frameCentre[0],
                self.frameHeight*self.frameIndex[1]+self.frameCentre[1]),
            (self.frameWidth, self.frameHeight),
            position.getP(),
            (d_width, d_height)
        )
