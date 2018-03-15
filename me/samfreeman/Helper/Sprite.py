# Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from me.samfreeman.Helper.Clock import Clock


class Sprite:
    def __init__(self, path, rows=1, cols=1, needAnimation=False):
        if path != "":
            # Attempts to find a file at the specified path
            self.spritesheet = simplegui._load_local_image(path)
            self.path = path
            self.hasPath = True
        else: self.hasPath = False
        self.rows = rows
        self.cols = cols

        # Frame Information
        if self.hasPath:
            self.frameWidth = self.spritesheet.get_width() / self.cols
            self.frameHeight = self.spritesheet.get_height() / self.rows
            self.frameIndex = [0, 0]
            self.frameCentre = (self.frameWidth / 2, self.frameHeight / 2)

        # Animation Tools (Default Values)
        self.startOffset = (0,0)
        self.frameDuration = 5
        self.animationLength = self.cols
        self.multipleLines = False
        self.animateOnce = True
        self.isComplete = False
        self.needAnimation = needAnimation
        if self.needAnimation:
            self.clock = Clock()

    def animate(self, full=False):
        if self.needAnimation:
            # Assumes animation is in one line
            if self.clock.transition(self.frameDuration):
                if not full: self.frameIndex[1] = self.startOffset[1]
                self.frameIndex[0] = self.startOffset[0] + ((self.frameIndex[0] + 1)
                                      % (self.startOffset[0] // self.cols + self.animationLength))



                if self.frameIndex[0] == self.startOffset[0]:
                    # Reached the end of the line
                    if full:
                        print("here")
                        self.frameIndex[1] = (self.frameIndex[1] + 1) % (self.rows)
                    elif self.animateOnce:
                        self.isComplete = True
                    else: self.frameIndex[0] = self.startOffset[0]

    def stopAnimation(self):
        self.isComplete = True

    def startAnimation(self, speed = 0, multipleLines = False):
        self.multipleLines = multipleLines
        self.isComplete = False
        self.frameDuration = self.frameDuration if speed == 0 else speed

    def updateInfo(self, frameDuration, start, length, reset, animateOnce):
        self.frameDuration = frameDuration
        self.startOffset = start
        self.animationLength = length
        self.animateOnce = animateOnce
        if reset and self.needAnimation: self.clock.time = 0

    # Allows for user to update just the frame index
    def setIndex(self, index):
        self.frameIndex = index

    # Returns a single frame sprite using the current sprite sheet
    def spriteFromIndex(self, index):
        newSprite = Sprite(self.path)
        newSprite.frameWidth = self.frameWidth
        newSprite.frameHeight = self.frameHeight
        newSprite.frameCentre = (newSprite.frameWidth / 2, newSprite.frameHeight / 2)
        newSprite.frameIndex = index
        return newSprite

    def draw(self, position, canvas, width=0, height=0):
        # Target width and height
        # If no width or height is specified, it will display the full size of the image
        d_width = width if width > 0 else self.frameWidth
        d_height = height if height > 0 else self.frameHeight

        # Draw the image
        canvas.draw_image(
            self.spritesheet,
            (self.frameWidth * self.frameIndex[0] + self.frameCentre[0],
             self.frameHeight * self.frameIndex[1] + self.frameCentre[1]),
            (self.frameWidth, self.frameHeight),
            position.getP(),
            (d_width, d_height)
        )

        # Animate
        if not self.isComplete:
                self.animate(self.multipleLines)

        # Update the clock
        if self.needAnimation: self.clock.tick()
