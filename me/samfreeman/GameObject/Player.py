from me.samfreeman.GameObject.GameObject import GameObject
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameObject.Projectiles import Projectile
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Helper.Line import Line
from me.samfreeman.GameObject.FireBalls import FireBall
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Player(GameObject):
    def __init__(self, position, sprite, frame, state, health=100, velocity=Vector((0, 0)), runSpeed=2, jumpSpeed=20):
        GameObject.__init__(self, position, velocity, [30, 90], health, sprite)
        self.runSpeed = runSpeed
        self.jumpSpeed = jumpSpeed
        self.animation = 0
        self.maxUnlockedWeapon = 2
        self.numberOfDeaths = 0
        self.state = state
        self.frame = frame

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
        self.swordHit = False

        self.diamondPickUp = Sprite("images/interactive-sprites/player/Player_UnlockingDiamond.png", 2, 10, True)
        self.firePickUp = Sprite("images/interactive-sprites/player/Player_UnlockingFire.png", 3, 8, True)
        self.gunPickUp = Sprite("images/interactive-sprites/player/Player_UnlockingGun.png", 3, 6, True)
        self.weaponPickUpSprite = self.diamondPickUp
        self.pickUpCounter = 0
        self.pickingUp = False

        #records if damage has been dealt this jump
        self.jumpHit = False

        self.offset = 0
        self.distanceFromFloor = 0 # used for crouching

        # So that the player does not get too fast
        self.maxVel = [3, 3]

        self.attackingSword = False
        self.attackingFire = False

        self.currentSprite = sprite

        # All Sprite Information
        self.animationLengthStand = 7
        self.animationLengthWalk = 8
        self.animationLengthCrouch = 7
        self.animationLengthAttack = 9
        self.animationLengthJumpUp = 4
        self.animationLengthJumpDown = 6

        self.directionState = GV.RIGHT
        self.currentAnimationLength = self.animationLengthStand
        self.actionState = GV.STANDING
        self.oldActionState = GV.STANDING
        self.frameWidthHeight = 60

        # Y is multiplied by 6 as that's the number of player states
        self.currentSpriteStart = [(self.directionState * self.currentAnimationLength * self.frameWidthHeight),
                                   ((self.maxUnlockedWeapon * 6 + self.actionState) * self.frameWidthHeight)]

        # Jump Testing
        self.hasJumped = False
        self.startingY = 0
        self.gravity = 1
        self.onGround = True # TODO: ADD PROPER FUNCTIONALITY TO THIS SO IT WORKS WITH PLATFORMS

        self.collectedCoins = 0

        self.wasHit = False
        self.flash = simplegui._load_local_image("images/interactive-sprites/display/damage-flash.png")
        self.counter = 0

        self.addAmount =0

    def displayHit(self):
        self.wasHit = True

    def moveLeft(self):

        if(self.canMoveLeft):
            self.offset = 0
            self.distanceFromFloor = 0
            self.dimensions[1] = 90

            if (self.animation == 1):
              # This line limits the maximum velocity
                if self.velocity.x <= -self.maxVel[0]:
                    self.velocity.x = -self.maxVel[0]
                self.velocity.add(Vector((-self.runSpeed / 2, 0)))
            else:
                if self.velocity.x <= -self.maxVel[0]:
                    self.velocity.x = -self.maxVel[0]
                else: self.velocity.add(Vector((-self.runSpeed, 0)))

            self.updateStates(GV.LEFT, self.animationLengthWalk, GV.WALKING, 5)

    def moveRight(self):
        if(self.canMoveRight):
            self.offset = 0
            self.distanceFromFloor = 0
            self.dimensions[1] = 90

            if (self.animation == 1):
                if self.velocity.x >= self.maxVel[0]:
                    self.velocity.x = self.maxVel[0]
                self.velocity.add(Vector((self.runSpeed / 2, 0)))
            else:
                if self.velocity.x >= self.maxVel[0]:
                    self.velocity.x = self.maxVel[0]
                else: self.velocity.add(Vector((self.runSpeed, 0)))

            self.updateStates(GV.RIGHT, self.animationLengthWalk, GV.WALKING, 5)

    def jump(self):
        if not self.hasJumped:
            self.gravity = 1
            self.startingY = self.position.y
            self.velocity.y = -20
            self.hasJumped = True
            self.checkPosition = True

    def crouch(self):
        self.offset = 0
        self.dimensions[1] = 60
        self.distanceFromFloor = self.dimensions[1] / 4

        self.updateStates(self.directionState, self.animationLengthCrouch, GV.CROUCHING, 3)

    def stand(self):
        self.offset = 0
        self.dimensions[1] = 90
        self.distanceFromFloor = 0

        self.updateStates(self.directionState, self.animationLengthStand, GV.STANDING, 8)

    def update(self):

        if self.velocity.y != 0:
            self.actionState = GV.JUMP_UP if self.velocity.y < 0 else GV.JUMP_DOWN
            self.currentAnimationLength = self.animationLengthJumpUp if self.velocity.y < 0 else self.animationLengthJumpDown
            self.updateStates(self.directionState, self.currentAnimationLength, self.actionState, 1)

        if self.attackingSword and 3 + self.currentSpriteStart[0] <= self.currentSprite.frameIndex[0] <= 6 + self.currentSpriteStart[0]:
            self.swordBBoxMove = True
        else:
            self.swordBBoxMove = False

        # Moves the sword (end-point) down
        if self.swordBBoxMove:
            self.addAmount = 7
        else:
            if self.addAmount !=0:
                self.swordHit = False
            self.addAmount = 0
            self.swordEndPoint.y = self.boundingBox.top


        if self.attackingSword:
            self.swordEndPoint = Vector((self.position.x + self.swordLength, self.swordEndPoint.y + self.addAmount))
            self.swordBoundingBox.pointA = self.position
            self.swordBoundingBox.pointB = self.swordEndPoint
            # self.swordBoundingBox = Line(self.position, self.swordEndPoint, 3)
        else:
            self.swordBoundingBox.pointA = Vector()
            self.swordBoundingBox.pointB = Vector()

        if self.currentSprite.isComplete:
            self.attackingSword = False
            self.swordHit = False
            self.attackingFire = False

        if(self.boundingBox.left > 10) and self.boundingBox.right < GV.CANVAS_WIDTH -20:
            GameObject.update(self)
        #stops sticking to LHS wall
        elif (self.velocity.x < 0 and self.boundingBox.left <= 10) or (self.boundingBox.right > GV.CANVAS_WIDTH -20 and self.velocity.x>0):
            self.velocity.x *=-2
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

        else: self.onGround = False

        if self.canMoveDown:
            self.velocity.y += self.gravity
        if self.onGround:
            self.velocity.y = 0
            self.startingY = self.currentGround - self.distanceFromFloor - self.dimensions[1] / 2# This will need to be the position of the platform or ground
            self.hasJumped = False

    def shoot(self):
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        self.projectiles.append(Projectile(self.position.copy(), 300, self.directionState))

    def swordAttack(self):
        self.attackingSword = True
        if self.directionState == GV.LEFT:
            self.offset = -30
            self.swordLength = -60
        else:
            self.offset = 30
            self.swordLength = 60

        self.updateStates(self.directionState, self.animationLengthAttack, GV.ATTACKING, 3, 1)

    def fireballAttack(self):
        self.attackingFire = True
        self.updateStates(self.directionState, self.animationLengthStand, GV.ATTACKING, 3, 1)
        if len(self.fireballs) == self.MAXIMUM_FIREBALLS: return
        self.fireballs.append(FireBall(self.position.copy(), self.velocity.copy(), self.directionState, self.dimensions[0] / 2))

    def updateStates(self, direction, aLen, act, speed=3, attack=0):
        self.currentAnimationLength = aLen
        self.oldActionState = self.actionState
        self.actionState = act
        self.directionState = direction

        print(self.actionState)
        if self.actionState == GV.ATTACKING and (self.maxUnlockedWeapon >= 2 and self.attackingFire):
            self.currentSpriteStart = [(self.directionState * self.currentAnimationLength),((15))]
        else:
            self.currentSpriteStart = [(self.directionState * self.currentAnimationLength),((1 * 6 + self.actionState))]

        if self.oldActionState != self.actionState:
            self.currentSprite.frameIndex = self.currentSpriteStart
            reset = True
        else: reset = False

        once = True if self.actionState == GV.ATTACKING else False

        self.currentSprite.updateInfo(speed, self.currentSpriteStart, self.currentAnimationLength,
                                        reset, once)
        self.currentSprite.startAnimation()

    def weaponPickUp(self):
        if self.pickUpCounter == 1:
            self.weaponPickUpSprite = self.firePickUp
        elif self.pickUpCounter == 2:
            self.weaponPickUpSprite = self.gunPickUp
        self.pickingUp = True
        self.weaponPickUpSprite.startAnimation(5, True)
    # Two methods to make sure that the player slows down
    # Might be equivalent to the standStill() method, not sure
    def notMoving(self):
        return self.velocity.length() == 0

    def stop(self):
        self.velocity.x = 0

    def draw(self, canvas, colour, position=Vector()):
        # print(self.currentSprite.frameIndex)
        if self.wasHit:
            self.counter += 1
            canvas.draw_image(self.flash, [GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2], [GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT], [GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2], [GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT])
            if self.counter >= 5:
                self.wasHit = False
                self.counter = 0
        if self.pickingUp:
            self.weaponPickUpSprite.draw(self.position, canvas, 90, 90)
            if self.weaponPickUpSprite.isComplete:
                self.state.playToWeapon()
                self.pickingUp = False
                self.pickUpCounter += 1
        else:
            GameObject.draw(self, canvas, colour, Vector((self.position.x + self.offset, self.position.y)), 90)
        # self.diamondPickUp.draw(position, canvas, 90, 90)
        if GV.bounding_box:
            self.swordBoundingBox.draw(canvas)
