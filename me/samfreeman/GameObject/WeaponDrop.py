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

    def collided(self):
        self.state.playToWeapon()

    def notifyUser(self, canvas):
        content = Rectangle(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2)), GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT * 0.5)
        content.draw(canvas, "White", "White")
        canvas.draw_text(self.title, ((GV.CANVAS_WIDTH - self.titleWidth) / 2, GV.CANVAS_HEIGHT / 6), 40, "White")
        self.weaponSprite.draw(content.position, canvas, 100, 100)
        unlock = "Congratulations! You have unlocked " + self.name
        unlockWidth = self.frame.get_canvas_textwidth(unlock, 20)
        canvas.draw_text(unlock, ((GV.CANVAS_WIDTH - unlockWidth) / 2, content.position.y + 60, 20, "Black"))

    def draw(self, canvas):
        if self.state.weaponPickUp:
            self.pickUpAnimation.draw(self.position, canvas)
            self.pickUpAnimation.startAnimation(6, True)
            if self.pickUpAnimation.isComplete:
                # Draw the weapon pickup stuff
                self.notifyUser()
        else:
            self.weaponSprite.draw(
                Vector((self.position.x, self.position.y + self.weaponSprite.dimensions[1])),
                canvas, self.weaponSprite.dimensions[0] * 2, self.weaponSprite.dimensions[1] * 2)