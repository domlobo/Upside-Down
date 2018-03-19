# Imports
from me.samfreeman.GameObject.Collectible import Collectible
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite


class Coin(Collectible):
    def __init__(self, position, size, value=1):
        print(value)
        Collectible.__init__(self, 0, position, size, Sprite("images/interactive-sprites/display/coin.png", 1, 12))
        self.value = value

    def pickUp(self, coins):
        Collectible.pickUp(self)
        return coins + self.value
