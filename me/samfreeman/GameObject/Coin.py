# Imports
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite


class Coin(GameObject):
    def __init__(self, position, size, value=1):
        GameObject.__init__(self, position, Vector(), [size, size], 1, Sprite("images/interactive-sprites/display/coin.png", 1, 12))
        self.value = value
        self.size = size

    def pickUp(self, coins):
        self.remove = True
        return coins + self.value

    def update(self, bgVel):
        self.position.x += bgVel.x

    def draw(self, canvas):
        self.sprite.draw(self.position, canvas, self.size, self.size)
        self.sprite.startAnimation(5)
