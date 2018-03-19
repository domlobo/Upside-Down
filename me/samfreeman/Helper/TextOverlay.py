# Imports
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite
import me.samfreeman.GameControl.GV as GV

class TextOverlay:
    def __init__(self, text, speaker):
        self.height = GV.CANVAS_HEIGHT * 0.2

        #link,player,unknown,mario,doom
        self.speakerOrder = [speaker]
        self.speakerList= ["Link", "Bob Froman", "Unknown", "Mario", "Doomslayer", "Ghost of Link"]
        self.speakerSpriteList = [simplegui._load_local_image("images/interactive-sprites/link/link-profile.png"),
                                    simplegui._load_local_image("images/cutscenes/Player_Profile.png"),
                                    simplegui._load_local_image("images/cutscenes/unknown.png"),
                                    simplegui._load_local_image("images/interactive-sprites/mario/mario-profile.png"),
                                    simplegui._load_local_image("images/interactive-sprites/doom/doom-profile.png"),
                                    simplegui._load_local_image("images/interactive-sprites/link/link-profile.png")]
        self.currentSpeakerIndex = 0
        self.currentSpeaker = self.speakerList[self.currentSpeakerIndex]
        self.BACKGROUND_LOAD = simplegui._load_local_image("images/background/TextOverlayBackground.png")
        self.BACKGROUND_HEIGHT = self.BACKGROUND_LOAD.get_height()
        self.BACKGROUND_WIDTH = self.BACKGROUND_LOAD.get_width()
        self.BACKGROUND_CENTER = Vector((self.BACKGROUND_WIDTH/2, self.BACKGROUND_HEIGHT/2))
        self.BACKGROUND_POSITION = Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT - self.height / 2))

        self.SPEAKER_POSITION = Vector((self.height * 0.5, self.BACKGROUND_POSITION.y))

        self.textWrap = Rectangle(Vector((GV.CANVAS_WIDTH * 0.2, self.BACKGROUND_POSITION.y)),
                                  GV.CANVAS_WIDTH,
                                  self.height)

        self.maxCharacterCount = 100
        self.text = [text]
        self.currentTextIndex = 0
        self.displayedText = self.text[self.currentTextIndex]

        self.continueText = "Press q to Continue..."
        self.done = False

    def nextText(self):
        self.done = (self.currentTextIndex == len(self.text))

        if not self.done:
            self.displayedText = self.text[self.currentTextIndex]
            self.currentSpeakerIndex = self.speakerOrder[self.currentTextIndex]
            self.currentSpeaker = self.speakerList[self.currentSpeakerIndex]
            self.currentSpeakerSprite = self.speakerSpriteList[self.currentSpeakerIndex]
            self.currentTextIndex += 1

    def addLine(self, line, speaker):
        # If the speaker doesn't change, they leave blank
        self.text.append(line)
        self.speakerOrder.append(speaker)

    def display(self, canvas):
        if not(self.done):
            #self.outline.draw(canvas, "White", "White")
            canvas.draw_image(self.BACKGROUND_LOAD,self.BACKGROUND_CENTER.getP(),(self.BACKGROUND_WIDTH,self.BACKGROUND_HEIGHT),self.BACKGROUND_POSITION.getP(),(self.BACKGROUND_WIDTH,self.height))

            speakerHeight = self.currentSpeakerSprite.get_height()
            speakerWidth = self.currentSpeakerSprite.get_width()
            speakerCenter= Vector((speakerWidth/2, speakerHeight/2))

            canvas.draw_image(self.currentSpeakerSprite,speakerCenter.getP(),(speakerWidth,speakerHeight),self.SPEAKER_POSITION.getP(),(speakerWidth,speakerHeight))
            canvas.draw_text(self.currentSpeaker, [self.SPEAKER_POSITION.x-(speakerWidth/2) ,self.SPEAKER_POSITION.y + (speakerHeight/2) - 20], 15, "Black", "monospace")
            canvas.draw_text(self.displayedText, self.textWrap.position.getP(), 15, "Black", "monospace")
            canvas.draw_text(self.continueText, [self.textWrap.position.x, GV.CANVAS_HEIGHT - 20], 15, "Black", "monospace")
