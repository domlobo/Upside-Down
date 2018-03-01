from GameObject import GameObject
from Vector import Vector
import GV


class Player(GameObject):
    def __init__(self, position, health=100, velocity=Vector((0, 0)), runSpeed=2, jumpSpeed=15):
        GameObject.__init__(self, position, velocity, [30, 60], health)
        self.runSpeed = runSpeed
        self.jumpSpeed = jumpSpeed
        self.weapon = 0
        self.direction = 0
        self.animation = 0
        self.maxUnlockedWeapon = 0

        # So that the player does not get too fast
        self.maxVel = [5, 5]

    # Haven't finished initialization.

    def moveLeft(self):
        self.direction = 1
        if (self.animation == 1):
            # This line limits the maximum velocity
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            self.velocity.add(Vector((-self.runSpeed / 2, 0)))
        else:
            if self.velocity.x <= -self.maxVel[0]:
                self.velocity.x = -self.maxVel[0]
            else: self.velocity.add(Vector((-self.runSpeed, 0)))

    def moveRight(self):
        self.direction = 2
        if (self.animation == 1):
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            self.velocity.add(Vector((self.runSpeed / 2, 0)))
        else:
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.add(Vector((self.runSpeed, 0)))

    def standStill(self):
        self.direction = 0

    def jump(self):
        if (self.position.y >= GV.CANVAS_HEIGHT - GV.EXTRA_JUMP_HEIGHT) and (self.velocity.y <= 0):
            if (self.animation == 1):
                self.velocity.add(Vector((0, -self.jumpSpeed / 2)))
            else:
                self.velocity.add(Vector((0, -self.jumpSpeed)))

    def changeWeapon(self, tryWeapon):
        if (tryWeapon <= self.maxUnlockedWeapon):
            self.weapon = tryWeapon

    def update(self):
        GameObject.update(self)
        self.velocity.multiply(0.85)

        if self.velocity.length() < 0.1: self.stop()

        if (self.position.y > GV.CANVAS_HEIGHT - self.dimensions[1] / 2):
            self.position.y = GV.CANVAS_HEIGHT - self.dimensions[1] / 2
            self.velocity.y = 0

            # if (self.weapon == 0) and (self.direction == 0) and (self.animation ==0):
            #	self.sprite.runningRight()
            # if (self.weapon == 0) and (self.direction == 0) and (self.animation ==0):
            #	self.sprite.runningLeft()
            # if (self.weapon == 0) and (self.direction == 0) and (self.animation ==0):
            #	self.sprite.jumping()

    # Two methods to make sure that the player slows down
    # Might be equivalent to the standStill() method, not sure
    def notMoving(self):
        return self.velocity.length() == 0

    def stop(self):
        self.velocity = Vector()
