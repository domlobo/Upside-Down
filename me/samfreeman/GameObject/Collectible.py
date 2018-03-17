from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Vector import Vector


class Collectible(GameObject):
    def __init__(self, type, position, size, sprite):
        GameObject.__init__(self, position, Vector(), [size, size], 1, sprite)
        self.size = size
        self.type = type

    def pickUp(self):
        self.remove = True

    def update(self, bgVel):
        self.position.x += bgVel.x

    def draw(self, canvas):
        self.sprite.draw(self.position, canvas, self.size, self.size)
