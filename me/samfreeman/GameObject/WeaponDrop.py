from me.samfreeman.GameControl import GV
from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Vector import Vector


class WeaponDrop:

    # Drop on the ground where enemy died
    # Animate picking up sword
    # Notify user
    # Cutscene

    def __init__(self, position, weaponSprite, pickUpAnimation, state, frame, name):
        self.position = position
        self.weaponSprite = weaponSprite
        self.pickUpAnimation = pickUpAnimation
        self.state = state
        self.frame = frame
        self.name = name
        self.title = "Weapon Unlocked!"
        self.titleWidth = self.frame.get_canvas_textwidth(self.title, 40)
        self.animate = False
        self.isAnimating = False

    def collided(self):
        self.animate = True
        # self.state.playToWeapon()

    def notifyUser(self, canvas):
        content = Rectangle(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2)), GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT * 0.5)
        content.draw(canvas, "White", "White")
        canvas.draw_text(self.title, ((GV.CANVAS_WIDTH - self.titleWidth) / 2, GV.CANVAS_HEIGHT / 6), 40, "White")
        self.weaponSprite.draw(content.position, canvas, 100, 100)
        unlock = "Congratulations! You have unlocked " + self.name
        unlockWidth = self.frame.get_canvas_textwidth(unlock, 20)
        canvas.draw_text(unlock, ((GV.CANVAS_WIDTH - unlockWidth) / 2, content.position.y + 60, 20, "Black"))

    def draw(self, canvas):
        # print("Drawing")
        if self.state.weaponPickUp:
            self.pickUpAnimation.draw(Vector((200, 200)),canvas, 200, 200)
            self.pickUpAnimation.startAnimation(8, True)
            # self.pickUpAnimation.draw(self.position, canvas, 200, 200)
            # if not self.isAnimating:
            #     print("Animating")
            #     self.pickUpAnimation.startAnimation(8, True)
            #     self.isAnimating = True
            # if self.pickUpAnimation.isComplete:
            #     print("Done")
            #     self.isAnimating = False
            #     self.state.playToWeapon()
        else:
            self.weaponSprite.draw(
                Vector((self.position.x, self.position.y + self.weaponSprite.frameHeight * 2)),
                canvas, self.weaponSprite.frameWidth, self.weaponSprite.frameHeight)