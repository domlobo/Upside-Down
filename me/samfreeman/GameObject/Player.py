from me.samfreeman.GameObject.GameObject import GameObject
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameObject.Projectiles import Projectile
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite

class Player(GameObject):
    def __init__(self, position, sprite, health=100, velocity=Vector((0, 0)), runSpeed=2, jumpSpeed=20):
        GameObject.__init__(self, position, velocity, [120, 120], health, sprite)
        self.runSpeed = runSpeed
        self.jumpSpeed = jumpSpeed
        self.weapon = 0
        self.direction = 0
        self.oldDirection = 2
        self.animation = 0
        self.maxUnlockedWeapon = 0

        self.projectiles = []
        self.MAXIMUM_PROJECTILES = 10

        # So that the player does not get too fast
        self.maxVel = [3, 3]

        self.currentSprite = sprite
        self.standingRight = Sprite("images/interactive-sprites/player/stand_right.png")
        self.walkingRight = Sprite("images/interactive-sprites/player/walk_right.png", True, 1, 8)
        self.walkingLeft = Sprite("images/interactive-sprites/player/walk_left.png", True, 1, 8)
        self.swordRight = Sprite("images/interactive-sprites/player/sword_right.png", True, 1, 8)
        self.swordLeft = Sprite("images/interactive-sprites/player/sword_left.png", True, 1, 8)

    # Haven't finished initialization.

    def moveLeft(self):
        self.currentSprite = self.walkingLeft
        self.updateSprite(self.currentSprite)
        self.currentSprite.animate(5)

        self.direction = 1
        self.oldDirection = 1
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
        self.currentSprite = self.walkingRight
        self.updateSprite(self.currentSprite)
        self.currentSprite.animate(5)

        self.direction = 2
        self.oldDirection = 2
        if (self.animation == 1):
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            self.velocity.add(Vector((self.runSpeed / 2, 0)))
        else:
            if self.velocity.x >= self.maxVel[0]:
                self.velocity.x = self.maxVel[0]
            else: self.velocity.add(Vector((self.runSpeed, 0)))

    def jump(self):
        if (self.position.y >= GV.CANVAS_HEIGHT - GV.EXTRA_JUMP_HEIGHT) and (self.velocity.y <= 0):
            if (self.animation == 1):
                self.velocity.add(Vector((0, -self.jumpSpeed / 2)))
            else:
                self.velocity.add(Vector((0, -self.jumpSpeed)))

    def crouch(self):
        self.dimensions[1] = 60
        self.position.y = GV.CANVAS_HEIGHT - 100 - self.dimensions[1] / 2 - 1

    def stand(self):
        self.dimensions[1] = 120
        self.position.y = GV.CANVAS_HEIGHT - 100 - self.dimensions[1] / 2 - 1
        self.currentSprite.stopAnimating()
        self.currentSprite = self.standingRight

    def changeWeapon(self, tryWeapon):
        if (tryWeapon <= self.maxUnlockedWeapon):
            self.weapon = tryWeapon

    def update(self):
        if((self.boundingBox.right < GV.CANVAS_WIDTH-10)and (self.boundingBox.left > 10)) or ((self.boundingBox.right>= GV.CANVAS_WIDTH-10) and (self.velocity.x <0)) or ((self.boundingBox.left <=10)and (self.velocity.x>0)):
            GameObject.update(self)
        self.velocity.multiply(0.85)

        if abs(self.velocity.x) < 0.1: self.stop()

        if (self.position.y > GV.CANVAS_HEIGHT - self.dimensions[1] / 2):
            self.position.y = GV.CANVAS_HEIGHT - self.dimensions[1] / 2
            self.velocity.y = 0

            # if (self.weapon == 0) and (self.direction == 0) and (self.animation ==0):
            #	self.sprite.runningRight()
            # if (self.weapon == 0) and (self.direction == 0) and (self.animation ==0):
            #	self.sprite.runningLeft()
            # if (self.weapon == 0) and (self.direction == 0) and (self.animation ==0):
            #	self.sprite.jumping()

        # Projectiles
        for proj in self.projectiles[:]:
            proj.update()
            if proj.remove: self.projectiles.remove(proj)

    def shoot(self):
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        self.projectiles.append(Projectile(self.position.copy(), 300, self.oldDirection))

    # Two methods to make sure that the player slows down
    # Might be equivalent to the standStill() method, not sure
    def notMoving(self):
        return self.velocity.length() == 0

    def stop(self):
        self.direction = 0
        self.velocity = Vector()
