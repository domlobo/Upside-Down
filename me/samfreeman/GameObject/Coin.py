# Imports
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Vector import Vector


class Coin(GameObject):
    def __init__(self, position, size, sprite, value=1):
        GameObject.__init__(self, position, Vector(), [size, size], sprite)
        self.value = value

    def pickUp(self, coins):
        self.remove = True
        return coins + self.value

    
