# Imports
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Vector import Vector
import me.samfreeman.GameControl.GV as GV

class TextOverlay:
    def __init__(self, text, speaker):
        self.height = GV.CANVAS_HEIGHT * 0.2
        self.outline = Rectangle(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT - self.height / 2)),
                                 GV.CANVAS_WIDTH,
                                 self.height)
        self.textWrap = Rectangle(Vector((GV.CANVAS_WIDTH * 0.2, self.outline.position.y)),
                                  GV.CANVAS_WIDTH,
                                  self.height)

        self.speakerList = [speaker]
        self.currentSpeakerIndex = 0
        self.currentSpeaker = self.speakerList[self.currentSpeakerIndex]
        self.speakerImg = Rectangle(Vector((self.height * 0.5, self.outline.position.y)),
                                    self.height * 0.5,
                                    self.height * 0.5)
        self.maxCharacterCount = 100
        self.text = [text]
        self.currentTextIndex = 0
        self.displayedText = self.text[self.currentTextIndex]

        self.continueText = "Press Space to Continue..."
        self.done = False

    def separateText(self):
        # Takes the text, and separates into lines
        # Will need to cycle through the text list, and pass current text into current text, display it, wait for space to be pressed.
        pass

    def nextText(self):
        if not self.done:
            self.currentTextIndex += 1
            self.displayedText = self.text[self.currentTextIndex]
            self.currentSpeakerIndex += 1
            self.currentSpeaker = self.speakerList[self.currentSpeakerIndex]
            self.done = (self.currentTextIndex == len(self.text) - 1)

    def addLine(self, line, speaker=""):
        # If the speaker doesn't change, they leave blank
        self.text.append(line)
        if speaker == "":
            self.speakerList.append(self.currentSpeaker)
        else:
            self.speakerList.append(speaker)

    def display(self, canvas):
        self.outline.draw(canvas, "White", "White")
        self.speakerImg.draw(canvas, "Black", "Black")
        canvas.draw_text(self.currentSpeaker, [self.speakerImg.left, self.speakerImg.top - 5], 15, "Black")
        canvas.draw_text(self.displayedText, self.textWrap.position.getP(), 15, "Black")
        canvas.draw_text(self.continueText, [self.textWrap.position.x, GV.CANVAS_HEIGHT - 15], 15, "Black")