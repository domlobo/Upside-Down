# Imports
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite
import me.samfreeman.GameControl.GV as GV


class FireBall(GameObject):
    def __init__(self, position, velocity, direction, offset, damage =10):
        if direction == GV.RIGHT:
            self.shootVel = Vector((2 + velocity.x, 0))
            position.x += offset
        else:
            self.shootVel = Vector((-2 + velocity.x, 0))
            position.x -= offset

        GameObject.__init__(self, position, self.shootVel, [60, 60], 50, Sprite(
                                                                            "images/interactive-sprites/mario/fireball.png",
                                                                             1, 11, True))
        self.gravity = 0.5
        self.bounceCount = 0
        self.damage = damage

    def drop(self, ground):
        self.velocity.y += self.gravity
        if self.position.y >= ground:
            self.velocity.reflect(Vector((0, -1))) # may need to change to -1
            self.bounceCount += 1

    def update(self, ground=0):
        GameObject.update(self)
        self.drop(500)
        self.sprite.startAnimation(5)
        if self.bounceCount >= 3: self.remove = True
        self.changeHealth(-1)
