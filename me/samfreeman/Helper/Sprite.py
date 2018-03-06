# Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from me.samfreeman.Helper.Clock import Clock


class Sprite:
    def __init__(self, assetPath, isSpriteSheet = False, rows=1, cols=1):
        if assetPath != "":
            self.image = simplegui._load_local_image(assetPath)
            self.loaded = True
        else: self.loaded = False
        self.isSpriteSheet = isSpriteSheet
        self.rows = rows
        self.cols = cols

        # Display Information
        if self.loaded:
            self.frameWidth = self.image.get_width() / self.cols
            self.frameHeight = self.image.get_height() / self.rows
            self.frameIndex = [0, 0]
            self.frameCentre = (self.frameWidth / 2, self.frameHeight / 2)

        self.animationClock = Clock()
        #self.fullAnimationClock = Clock()
        self.isAnimating = 0
        self.needTick = False

        print(assetPath)

    def animate(self, frameDuration):
        # Will animate while it is being called (such as moving a player)
        self.needTick = True
        if self.animationClock.transition(frameDuration):
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.cols
            if self.frameIndex[0] == 0:
                self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows

    def animateFull(self, frameDuration):
        # Will animate without moving (go through entire sprite sheet)
        self.needTick = True
        if self.animationClock.transition(frameDuration):
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.cols
            if self.frameIndex[0] == 0:
                self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows
                if self.frameIndex[1] == 0: self.isAnimating = 0

    def setAnimating(self, frameDuration):
        self.isAnimating = frameDuration

    def stopAnimating(self):
        self.needTick = False

    def setIndex(self, index):
        self.frameIndex = index

    def draw(self, position, canvas, width=0, height=0):
        # Target width and height
        # If no width or height is specified, it will display the full size of the image
        d_width = self.image.get_width()  # Destination width
        d_height = self.image.get_height()  # Destination height
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
            (self.frameWidth, self.frameWidth),
            position.getP(),
            (d_width, d_height)
        )

        # print("f_width " + str(self.frameWidth))
        # print("f_index " + str(self.frameIndex))
        # print("f_height " + str(self.frameHeight))
        # print("f_centre " + str(self.frameCentre))
        # print("pos " + str(position.getP()))