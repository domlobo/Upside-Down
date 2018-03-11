# Imports
from me.samfreeman.GameControl import GV
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.Helper.Vector import Vector


class Cutscene:
    def __init__(self):
        self.numberOfSpeakers = [2] # Use 1 or 2

        self.gapSize = GV.CANVAS_WIDTH / 12

        # LHS
        self.leftSpeaker = []
        self.leftSprite = []
        self.leftAllText = []
        self.leftLineNumber = 0

        # RHS
        self.rightSpeaker = [""]
        emptySprite = Sprite("")
        emptySprite.frameWidth = 100
        emptySprite.frameHeight = 100
        self.rightSprite = [emptySprite]
        self.rightAllText = [""]
        self.rightLineNumber = 0

        # Display
        self.contentBoundingBox = Rectangle(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2)), GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT * 0.5)
        self.leftBoundingBox = Rectangle(Vector((self.contentBoundingBox.left + GV.CANVAS_WIDTH / 4, self.contentBoundingBox.position.y)), GV.CANVAS_WIDTH / 2, self.contentBoundingBox.height)
        self.rightBoundingBox = Rectangle(Vector((self.contentBoundingBox.right - GV.CANVAS_WIDTH / 4, self.contentBoundingBox.position.y)), GV.CANVAS_WIDTH / 2, self.contentBoundingBox.height)

    def addText(self, personA, personAText, personASprite, personB="", personBText="", personBSprite=""):
        if personB != "":
            # There are two people
            self.numberOfSpeakers.append(2)
            self.rightSpeaker.append(personB)
            self.rightAllText.append(personBText)
            self.rightSprite.append(personBSprite)

        self.numberOfSpeakers.append(1)
        self.leftSpeaker.append(personA)
        self.leftAllText.append(personAText)
        self.leftSprite.append(personASprite)

    def nextLine(self):
        print("Updated")
        # This needs to be fixed as it will fall apart if it goes from 2 --> 1 speaker
        if (self.rightLineNumber < len(self.rightSpeaker) - 1):
            if (self.leftLineNumber < self.rightLineNumber):
                # Update Left Text
                self.leftLineNumber += 1
                # if self.numberOfSpeakers == 1:
                #     self.leftBoundingBox = Rectangle(self.contentBoundingBox.position.copy(), self.contentBoundingBox.width, self.contentBoundingBox.height)
            else:
                # Update Right
                self.rightLineNumber += 1
                # self.leftBoundingBox = Rectangle(
                #     Vector((self.contentBoundingBox.left + GV.CANVAS_WIDTH / 4, self.contentBoundingBox.position.y)),
                #     GV.CANVAS_WIDTH / 2, self.contentBoundingBox.height)
                # self.rightBoundingBox = Rectangle(
                #     Vector((self.contentBoundingBox.right - GV.CANVAS_WIDTH / 4, self.contentBoundingBox.position.y)),
                #     GV.CANVAS_WIDTH / 2, self.contentBoundingBox.height)

    def clear(self):
        # Clears/resets all content
        # LHS
        self.leftSpeaker = []
        self.leftSprite = []
        self.leftAllText = []
        self.leftLineNumber = 0

        # RHS
        self.rightSpeaker = [""]
        emptySprite = Sprite("")
        emptySprite.frameWidth = 100
        emptySprite.frameHeight = 100
        self.rightSprite = [emptySprite]
        self.rightAllText = [""]
        self.rightLineNumber = 0

    def splitText(self, text, people):
        maxCharacters = 24 if people == 2 else 48
        return [text[i:i+maxCharacters] for i in range(0, len(text), maxCharacters)]

    def drawCutSceneText(self, startY, text, canvas, lOrR, people):
        textLines = self.splitText(text, people)
        offset = self.gapSize + 50
        if not lOrR: offset = self.rightBoundingBox.left + 50
        i = 0
        for line in textLines:
            canvas.draw_text(line, (offset, startY+15 * i), 12, "Black", "monospace")
            i+=1

    def drawLeft(self, canvas):
        self.leftSprite[self.leftLineNumber].draw(Vector((self.gapSize, self.leftBoundingBox.position.y)), canvas, 100, 100)
        canvas.draw_text(self.leftSpeaker[self.leftLineNumber], (self.gapSize / 2, self.leftBoundingBox.position.y - 100 / 2),
                         15, "Black", "monospace")
        self.drawCutSceneText(self.contentBoundingBox.top + self.gapSize * 2, self.leftAllText[self.leftLineNumber], canvas, True, self.numberOfSpeakers[self.leftLineNumber])

    def drawRight(self, canvas):

        self.rightSprite[self.rightLineNumber].draw(Vector((self.rightBoundingBox.right - self.gapSize, self.rightBoundingBox.position.y)), canvas, 100, 100)
        canvas.draw_text(self.rightSpeaker[self.rightLineNumber], (self.rightBoundingBox.right - self.gapSize, self.rightBoundingBox.position.y - 100 / 2),
                         15, "Black", "monospace")
        self.drawCutSceneText(self.contentBoundingBox.top + self.gapSize * 2, self.rightAllText[self.rightLineNumber], canvas, False, self.numberOfSpeakers[self.leftLineNumber])

    def display(self, canvas):
        self.contentBoundingBox.draw(canvas, "White", "White")
        self.drawLeft(canvas)
        if self.numberOfSpeakers[self.leftLineNumber] == 2 and self.rightLineNumber > 0:
            # Two speakers -- draw right
            self.drawRight(canvas)
            # Draw Line
            canvas.draw_line((self.contentBoundingBox.position.x - self.gapSize, self.contentBoundingBox.bottom),
                             (self.contentBoundingBox.position.x + self.gapSize, self.contentBoundingBox.top), 5, "Black")