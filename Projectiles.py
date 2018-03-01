# imports
from GameObject import GameObject
from Vector import Vector
import GV


class Projectile(GameObject):
    def __init__(self, position, lifetime, direction):
        GameObject.__init__(self, position, Vector((0, 0)), [20, 5], lifetime)

        self.direction = direction
        self.damage = 10
        self.speed = 1.7
        self.maxVel = [8, 8]

    def update(self):
        GameObject.update(self)
        if self.direction == GV.RIGHT:
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.x += self.speed
        if self.direction == GV.LEFT:
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else: self.velocity.x -= self.speed

        self.changeHealth(-3)