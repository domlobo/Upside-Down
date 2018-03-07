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
        self.oldDirection = 2
        self.animation = 0
        self.maxUnlockedWeapon = 0

        self.projectiles = []
        self.MAXIMUM_PROJECTILES = 10

        # So that the player does not get too fast
        self.maxVel = [3, 3]

        self.attackingSword = False

        self.currentSprite = sprite

        # Wooden Sword Sprites
        self.bobbingRight_wSword = Sprite("images/interactive-sprites/player/wooden-sword/bobbing_right_wsword.png", True, 1, 7)
        self.bobbingLeft_wSword = Sprite("images/interactive-sprites/player/wooden-sword/bobbing_left_wsword.png", True, 1, 7)
        self.walkingRight_wSword = Sprite("images/interactive-sprites/player/wooden-sword/movement_right_wsword.png", True, 1, 8)
        self.walkingLeft_wSword = Sprite("images/interactive-sprites/player/wooden-sword/movement_left_wsword.png", True, 1, 8)
        self.attackRight_wSword = Sprite("images/interactive-sprites/player/wooden-sword/attack_right_wsword.png", True, 1, 9)
        self.attackLeft_wSword = Sprite("images/interactive-sprites/player/wooden-sword/attack_left_wsword.png", True, 1, 9)
        self.crouchRight_wSword = Sprite("images/interactive-sprites/player/wooden-sword/crouch_right_wsword.png", True, 1, 7)
        self.crouchLeft_wSword = Sprite("images/interactive-sprites/player/wooden-sword/crouch_left_wsword.png", True, 1, 7)

        # Link Sword Sprites
        self.bobbingRight_lSword = Sprite("images/interactive-sprites/player/link-sword/bobbing_right_lsword.png", True, 1, 7)
        self.bobbingLeft_lSword = Sprite("images/interactive-sprites/player/link-sword/bobbing_left_lsword.png", True, 1, 7)
        self.walkingRight_lSword = Sprite("images/interactive-sprites/player/link-sword/movement_right_lsword.png", True, 1, 8)
        self.walkingLeft_lSword = Sprite("images/interactive-sprites/player/link-sword/movement_left_lsword.png", True, 1, 8)
        self.attackRight_lSword = Sprite("images/interactive-sprites/player/link-sword/attack_right_lsword.png", True, 1, 9)
        self.attackLeft_lSword = Sprite("images/interactive-sprites/player/link-sword/attack_left_lsword.png", True, 1, 9)
        self.crouchRight_lSword = Sprite("images/interactive-sprites/player/link-sword/crouch_right_lsword.png", True, 1, 7)
        self.crouchLeft_lSword = Sprite("images/interactive-sprites/player/link-sword/crouch_left_lsword.png", True, 1, 7)

        # Gun Sprites
        self.attackRight_gun = Sprite("")
        self.attackLeft_gun = Sprite("")

        # Fire Sprites
        self.attackRight_fire = Sprite("")
        self.attackLeft_fire = Sprite("")

        # Used Animations
        self.bobbingRight = self.bobbingRight_wSword
        self.bobbingLeft = self.bobbingLeft_wSword

        self.walkingRight = self.walkingRight_wSword
        self.walkingLeft = self.walkingLeft_wSword
        self.attackRight = self.attackRight_wSword
        self.attackLeft = self.attackLeft_wSword
        self.crouchRight = self.crouchRight_wSword
        self.crouchLeft = self.crouchLeft_wSword

    # Haven't finished initialization.

    def setAnimationSet(self, set):
        if set == GV.WOODEN_SWORD:
            self.bobbingRight = self.bobbingRight_wSword
            self.bobbingLeft = self.bobbingLeft_wSword

            self.walkingRight = self.walkingRight_wSword
            self.walkingLeft = self.walkingLeft_wSword
            self.attackRight = self.attackRight_wSword
            self.attackLeft = self.attackLeft_wSword

            self.crouchRight = self.crouchRight_wSword
            self.crouchLeft = self.crouchLeft_wSword
        elif set == GV.SWORD:
            self.bobbingRight = self.bobbingRight_lSword
            self.bobbingLeft = self.bobbingLeft_lSword

            self.walkingRight = self.walkingRight_lSword
            self.walkingLeft = self.walkingLeft_lSword
            self.attackRight = self.attackRight_lSword
            self.attackLeft = self.attackLeft_lSword

            self.crouchRight = self.crouchRight_lSword
            self.crouchLeft = self.crouchLeft_lSword
        elif set == GV.GUN:
            self.attackRight = self.attackRight_gun
            self.attackLeft = self.attackLeft_gun
        elif set == GV.FIRE:
            self.attackRight = self.attackRight_fire
            self.attackLeft = self.attackLeft_fire

    def moveLeft(self):
        self.currentSprite = self.walkingLeft
        self.updateSprite(self.currentSprite)
        self.currentSprite.animate(5)

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
        self.position.y = GV.CANVAS_HEIGHT - 100 - self.dimensions[1] / 2 - 1
        if self.oldDirection == 1:
            self.currentSprite = self.crouchLeft
        else:
            self.currentSprite = self.crouchRight

        self.currentSprite.setAnimating(3)
        self.updateSprite(self.currentSprite)

    def stand(self):
        self.dimensions[1] = 120
        self.position.y = GV.CANVAS_HEIGHT - 100 - self.dimensions[1] / 2 - 1
        self.currentSprite = self.bobbingRight

        if self.oldDirection == 1:
            self.currentSprite = self.bobbingLeft
        else:
            self.currentSprite = self.bobbingRight

        self.currentSprite.setAnimating(8)
        self.updateSprite(self.currentSprite)

    def changeWeapon(self, tryWeapon):
        if (tryWeapon <= self.maxUnlockedWeapon):
            self.weapon = tryWeapon

    def update(self):
        if self.currentSprite.isAnimating == 0: self.attackingSword = False

        if((self.boundingBox.right < GV.CANVAS_WIDTH-10)and (self.boundingBox.left > 10)) or ((self.boundingBox.right>= GV.CANVAS_WIDTH-10) and (self.velocity.x <0)) or ((self.boundingBox.left <=10)and (self.velocity.x>0)):
            GameObject.update(self)
        self.velocity.multiply(0.85)

        if abs(self.velocity.x) < 0.1: self.stop()

        if (self.position.y > GV.CANVAS_HEIGHT - self.dimensions[1] / 2):
            self.position.y = GV.CANVAS_HEIGHT - self.dimensions[1] / 2
            self.velocity.y = 0

        # Projectiles
        for proj in self.projectiles[:]:
            proj.update()
            if proj.remove: self.projectiles.remove(proj)

        self.setAnimationSet(self.weapon)

    def shoot(self):
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        self.projectiles.append(Projectile(self.position.copy(), 300, self.oldDirection))

    def swordAttack(self):
        self.attackingSword = True
        if self.oldDirection == 1:
            self.currentSprite = self.attackLeft
        else:
            self.currentSprite = self.attackRight
        self.updateSprite(self.currentSprite)
        self.currentSprite.setAnimating(5)


    # Two methods to make sure that the player slows down
    # Might be equivalent to the standStill() method, not sure
    def notMoving(self):
        return self.velocity.length() == 0

    def stop(self):
        self.velocity = Vector()
