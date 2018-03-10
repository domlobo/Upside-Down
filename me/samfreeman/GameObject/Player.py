from me.samfreeman.GameObject.GameObject import GameObject
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameObject.Projectiles import Projectile
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.Helper.Line import Line
from me.samfreeman.GameObject.FireBalls import FireBall


class Player(GameObject):
    def __init__(self, position, sprite, health=100, velocity=Vector((0, 0)), runSpeed=2, jumpSpeed=20):
        GameObject.__init__(self, position, velocity, [90, 90], health, sprite)
        self.runSpeed = runSpeed
        self.jumpSpeed = jumpSpeed
        self.oldDirection = 2
        self.animation = 0
        self.maxUnlockedWeapon = 0

        # Weapon Stuff
        self.projectiles = []
        self.MAXIMUM_PROJECTILES = 10
        self.fireballs = []
        self.MAXIMUM_FIREBALLS = 10 # have one follow the other --> maybe have three come out when clicked

        # Sword stuff
        self.swordLength = 60
        self.swordDamage = 30
        self.swordEndPoint = Vector((self.position.x + self.swordLength, self.boundingBox.top))
        self.swordBoundingBox = Line(self.position, self.swordEndPoint, 3)
        self.maxSwordDown = self.boundingBox.bottom
        self.swordBBoxMove = False

        self.offset = 0
        self.distanceFromFloor = 0 # used for crouching

        # So that the player does not get too fast
        self.maxVel = [3, 3]

        self.attackingSword = False

        self.currentSprite = sprite

        # All Sprite Information
        self.animationLengthStand = 7
        self.animationLengthWalk = 8
        self.animationLengthCrouch = 7
        self.animationLengthAttack = 9

        self.directionState = GV.RIGHT # TODO: will update to "self.direction" when working
        self.currentAnimationLength = self.animationLengthStand
        self.weapon = 1 # will need to update
        self.actionState = GV.STANDING
        self.oldActionState = GV.STANDING
        self.updatedFI = False
        self.frameWidthHeight = 60

        # Y is multiplied by 6 as that's the number of player states
        self.currentSpriteStart = [(self.directionState * self.currentAnimationLength * self.frameWidthHeight),
                                   ((self.weapon * 6 + self.actionState) * self.frameWidthHeight)]

        # Jump Testing
        self.hasJumped = False
        self.startingY = 0
        self.currentGround = self.position.y + self.dimensions[1] / 2
        self.gravity = 1
        self.onGround = True # TODO: ADD PROPER FUNCTIONALITY TO THIS SO IT WORKS WITH PLATFORMS

    def moveLeft(self):

        if(self.canMoveLeft):
            self.offset = 0
            self.distanceFromFloor = 0
            self.dimensions[1] = 90

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

            self.updateStates(GV.LEFT, self.animationLengthWalk, GV.WALKING)

    def moveRight(self):
        if(self.canMoveRight):
            self.offset = 0
            self.distanceFromFloor = 0
            self.dimensions[1] = 90

            self.oldDirection = 2
            if (self.animation == 1):
                if self.velocity.x >= self.maxVel[0]:
                    self.velocity.x = self.maxVel[0]
                self.velocity.add(Vector((self.runSpeed / 2, 0)))
            else:
                if self.velocity.x >= self.maxVel[0]:
                    self.velocity.x = self.maxVel[0]
                else: self.velocity.add(Vector((self.runSpeed, 0)))

            self.updateStates(GV.RIGHT, self.animationLengthWalk, GV.WALKING)

    def jump(self):
        if not self.hasJumped:
            self.gravity = 1
            self.startingY = self.position.y
            self.velocity.y = -20
            self.hasJumped = True

            # TODO: check if moving down or up and update the animation accordingly

    def crouch(self):
        self.offset = 0
        self.dimensions[1] = 60
        self.distanceFromFloor = self.dimensions[1] / 4

        self.updateStates(self.oldDirection % 2, self.animationLengthCrouch, GV.CROUCHING, 3, False)

    def stand(self):
        self.offset = 0
        self.dimensions[1] = 90
        self.distanceFromFloor = 0

        self.updateStates(self.oldDirection % 2, self.animationLengthStand, GV.STANDING, 8, False)

    def changeWeapon(self, tryWeapon):
        if (tryWeapon <= self.maxUnlockedWeapon):
            self.weapon = tryWeapon

    def update(self):

        if self.swordEndPoint.y >= self.maxSwordDown:
            self.swordEndPoint = Vector((self.position.x, self.boundingBox.top)) # so no collision

        if self.attackingSword and 3 + self.currentSpriteStart[0] <= self.currentSprite.frameIndex[0] <= 6 + self.currentSpriteStart[0]:
            self.swordBBoxMove = True
        else:
            self.swordBBoxMove = False

        if self.swordBBoxMove:
            addAmount = 7
        else:
            addAmount = 0
            self.swordEndPoint.y = self.boundingBox.top

        self.swordEndPoint = Vector((self.position.x + self.swordLength, self.swordEndPoint.y + addAmount))
        self.swordBoundingBox = Line(self.position, self.swordEndPoint, 3)
        if self.currentSprite.isAnimating == 0:
            self.attackingSword = False
            print("here")

        if((self.boundingBox.right < GV.CANVAS_WIDTH-10)and (self.boundingBox.left > 10)) or ((self.boundingBox.right>= GV.CANVAS_WIDTH-10) and (self.velocity.x <0)) or ((self.boundingBox.left <=10)and (self.velocity.x>0)):
            GameObject.update(self)
        self.velocity.multiply(0.85)

        if abs(self.velocity.x) < 0.1: self.stop()

        # Projectiles
        for proj in self.projectiles[:]:
            proj.update()
            if proj.position.x <=0  or proj.position.x >= GV.CANVAS_WIDTH:
                proj.remove = True
            if proj.remove: self.projectiles.remove(proj)

        for fireball in self.fireballs[:]:
            fireball.update(GV.CANVAS_HEIGHT - GV.FLOOR_HEIGHT)
            if fireball.remove:self.fireballs.remove(fireball)

        if self.position.y >= GV.CANVAS_HEIGHT - GV.FLOOR_HEIGHT:
            self.onGround = True
            self.position.y = GV.CANVAS_HEIGHT - GV.FLOOR_HEIGHT
        else: self.onGround = False

        # if self.position.y >= self.currentGround - self.distanceFromFloor - self.dimensions[1] / 2 and not self.onGround:
        #     self.position.y = self.currentGround - self.distanceFromFloor - self.dimensions[1] / 2

        if self.canMoveDown:
            self.velocity.y += self.gravity
        if self.onGround:
            self.velocity.y = 0
            self.startingY = self.currentGround - self.distanceFromFloor - self.dimensions[1] / 2# This will need to be the position of the platform or ground
            self.hasJumped = False

    def shoot(self):
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        self.projectiles.append(Projectile(self.position.copy(), 300, self.oldDirection))

    def swordAttack(self):
        self.attackingSword = True
        if self.oldDirection == 1:
            self.offset = -30
            self.swordLength = -60
        else:
            self.offset = 30
            self.swordLength = 60

        self.updateStates(self.oldDirection % 2, self.animationLengthAttack, GV.ATTACKING, 3)


    def fireballAttack(self):
        if len(self.fireballs) == self.MAXIMUM_FIREBALLS: return
        self.fireballs.append(FireBall(self.position.copy(), self.velocity.copy(), self.oldDirection % 2, self.dimensions[0] / 2))

    def updateStates(self, dir, aLen, act, speed=0, reset=True):
        self.currentAnimationLength = aLen
        self.oldActionState = self.actionState
        self.actionState = act
        self.directionState = dir

        self.currentSpriteStart = [(self.directionState * self.currentAnimationLength),
                                   ((self.weapon * 6 + self.actionState))]

        if self.oldActionState != self.actionState:
            self.currentSprite.frameIndex = self.currentSpriteStart

        if speed != 0:
            self.currentSprite.setAnimating(speed, self.currentSpriteStart, self.currentAnimationLength, reset)
        else: self.currentSprite.animate(5, self.currentSpriteStart, self.currentAnimationLength)

    # Two methods to make sure that the player slows down
    # Might be equivalent to the standStill() method, not sure
    def notMoving(self):
        return self.velocity.length() == 0

    def stop(self):
        self.velocity.x = 0

    def draw(self, canvas, colour, position=Vector()):
        GameObject.draw(self, canvas, colour, Vector((self.position.x + self.offset, self.position.y)))
        self.swordBoundingBox.draw(canvas)
