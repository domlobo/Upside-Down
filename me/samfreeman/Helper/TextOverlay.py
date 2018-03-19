# Imports
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Vector import Vector
import me.samfreeman.GameControl.GV as GV

class TextOverlay:
    def __init__(self, text, speaker):
        self.height = GV.CANVAS_HEIGHT * 0.2


        self.speakerList = [speaker]
        self.currentSpeakerIndex = 0
        self.currentSpeaker = self.speakerList[self.currentSpeakerIndex]
        self.BACKGROUND_LOAD = simplegui._load_local_image("images/background/TextOverlayBackground.jpg")
        self.BACKGROUND_HEIGHT = self.BACKGROUND_LOAD.get_height()
        self.BACKGROUND_WIDTH = self.BACKGROUND_LOAD.get_width()
        self.BACKGROUND_CENTER = Vector((self.BACKGROUND_WIDTH/2, self.BACKGROUND_HEIGHT/2))
        self.BACKGROUND_POSITION = Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT - self.height / 2))

        self.textWrap = Rectangle(Vector((GV.CANVAS_WIDTH * 0.2, self.BACKGROUND_POSITION.y)),
                                  GV.CANVAS_WIDTH,
                                  self.height)

        self.speakerImg = Rectangle(Vector((self.height * 0.5, self.BACKGROUND_POSITION.y)),
                                    self.height * 0.5,
                                    self.height * 0.5)
        self.maxCharacterCount = 100
        self.text = [text]
        self.currentTextIndex = 0
        self.displayedText = self.text[self.currentTextIndex]
        self.lastLevel = False
        self.continueText = "Press q to Continue..."
        self.done = False

    def nextText(self):
        self.done = (self.currentTextIndex == len(self.text)-1)

        if not self.done:
            self.currentTextIndex += 1
            self.displayedText = self.text[self.currentTextIndex]
            self.currentSpeakerIndex += 1
            self.currentSpeaker = self.speakerList[self.currentSpeakerIndex]

    def addLine(self, line, speaker=""):
        # If the speaker doesn't change, they leave blank
        self.text.append(line)
        if speaker == "":
            self.speakerList.append(self.currentSpeaker)
        else:
            self.speakerList.append(speaker)

    def display(self, canvas):
        if self.lastLevel:
            self.continueText = "Press L to SHOOT JESS!"
        if not(self.done):
            #self.outline.draw(canvas, "White", "White")
            canvas.draw_image(self.BACKGROUND_LOAD,self.BACKGROUND_CENTER.getP(),(self.BACKGROUND_WIDTH,self.BACKGROUND_HEIGHT),self.BACKGROUND_POSITION.getP(),(self.BACKGROUND_WIDTH,self.height))

            self.speakerImg.draw(canvas, "Black", "Black")
            canvas.draw_text(self.currentSpeaker, [self.speakerImg.left, self.speakerImg.top - 5], 15, "Black", "monospace")
            canvas.draw_text(self.displayedText, self.textWrap.position.getP(), 15, "Black", "monospace")
            canvas.draw_text(self.continueText, [self.textWrap.position.x, GV.CANVAS_HEIGHT - 20], 15, "Black", "monospace")
