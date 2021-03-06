from me.samfreeman.GameControl import GV
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite


class MainMenu:
    def __init__(self, frame):
        self.background = Sprite("images/background/link/link-background.jpg")
        self.floor = Sprite("images/background/link/link-floor.png")
        self.dancingSprite = Sprite("images/interactive-sprites/player/Player_Dance_Right.png", 6, 9, True)
        self.title = Sprite("images/background/title.png")
        self.startText = "Press Space to Play"
        self.startTextWidth = frame.get_canvas_textwidth(self.startText, 40, "monospace")

    def draw(self, canvas):
        self.background.draw(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2 + 40)), canvas, self.background.frameWidth, self.background.frameHeight + 150)
        self.floor.draw(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT)), canvas, self.floor.frameWidth, 100)
        self.dancingSprite.startAnimation(8, True)
        self.dancingSprite.draw(Vector((100, GV.CANVAS_HEIGHT - 150)), canvas, 200, 200)
        self.title.draw(Vector((GV.CANVAS_WIDTH / 2, 150)), canvas, GV.CANVAS_WIDTH * 5/6, self.title.frameHeight)
        canvas.draw_text(self.startText, ((GV.CANVAS_WIDTH - self.startTextWidth) / 2, GV.CANVAS_HEIGHT / 2), 40, "White", "monospace")
        canvas.draw_text("Press q when you die and see a black screen", ((GV.CANVAS_WIDTH - self.startTextWidth) / 2, GV.CANVAS_HEIGHT * 7/8), 30, "Black", "monospace")