# imports
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Vector import Vector


class Projectile(GameObject):
    def __init__(self, position, lifetime, direction,speed=1.7):
        GameObject.__init__(self, position, Vector((0, 0)), [20, 5], lifetime)

        self.direction = direction
        self.damage = 10
        self.speed = speed
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
