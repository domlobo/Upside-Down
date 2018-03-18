from me.samfreeman.GameObject.Collectible import Collectible
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Vector import Vector


class WeaponPickUp(Collectible):
    def __init__(self, position, player, weaponSprite):
        Collectible.__init__(self,1, position, 90, weaponSprite)
        self.player = player

    def pickUp(self):
        Collectible.pickUp(self)
        self.player.weaponPickUp()