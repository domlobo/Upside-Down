from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Vector import Vector


class WeaponPickUp(GameObject):
    def __init__(self, position, player, weaponSprite):
        GameObject.__init__(self, position, Vector(), [90, 90], 1, weaponSprite)
        self.player = player
        self.type = 1

    def pickUp(self):
        self.player.weaponPickUp()
        print("Picked Up")

    def update(self, bgVel):
        self.position.x += bgVel.x

    def draw(self, canvas):
        self.sprite.draw(self.position, canvas, 90, 90)