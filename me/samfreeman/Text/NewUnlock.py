from me.samfreeman.GameControl import GV
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.Helper.Vector import Vector


class NewUnlock:
    def __init__(self, frame):
        self.counter = 0
        self.diamondSwordSprite = Sprite("images/interactive-sprites/player/DiamondSword.png")
        self.fireSprite = Sprite("images/interactive-sprites/player/Fireball.png")
        self.gunSprite = Sprite("images/interactive-sprites/player/Gun.png")
        self.displaySprite = self.diamondSwordSprite

        self.frame = frame
        self.container = Rectangle(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2)), GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT * 2 / 5)

        self.title = "Link's Sword"
        self.button = "J"
        self.text = "Congratulations, you unlocked " + self.title + ". Use with key: " + self.button

        self.hasUpdated = False

    def display(self, canvas):
        self.container.draw(canvas, "White", "White")
        if self.counter == 1:
            self.title = "Mario's Fire"
            self.button = "K"
            self.displaySprite = self.fireSprite
        elif self.counter == 2:
            self.title = "BFG"
            self.button = "L"
            self.displaySprite = self.gunSprite
            
        self.text = "Congratulations, you unlocked " + self.title + ". Use with key: " + self.button
        title_width = self.frame.get_canvas_textwidth(self.title, 30)
        text_width = self.frame.get_canvas_textwidth(self.text, 20)
        canvas.draw_text(self.title, ((GV.CANVAS_WIDTH - title_width) / 2, GV.CANVAS_HEIGHT / 6), 30, "White")
        canvas.draw_text(self.text, ((GV.CANVAS_WIDTH - text_width) / 2, self.container.top + 50), 20, "Black")
        self.displaySprite.draw(self.container.position, canvas, 200, 200)
        continue_width = self.frame.get_canvas_textwidth("Press q To Continue", 20)
        canvas.draw_text("Press q To Continue...", ((GV.CANVAS_WIDTH - continue_width) / 2, GV.CANVAS_HEIGHT * 5/6), 20, "White")