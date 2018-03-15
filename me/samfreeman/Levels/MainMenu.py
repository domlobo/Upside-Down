from me.samfreeman.GameControl import GV
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite


class MainMenu:
    def __init__(self):
        self.background = Sprite("")
        self.dancingSprite = Sprite("images/interactive-sprites/player/Player_Dance_Right.png", 6, 9, True)

    def draw(self, canvas):
        # self.background.draw(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2)), canvas)
        canvas.draw_text("Play", (0, GV.CANVAS_HEIGHT / 2), 200,"White", "monospace")

        self.dancingSprite.startAnimation(8, True)

        self.dancingSprite.draw(Vector((100, 100)), canvas, 300, 300)