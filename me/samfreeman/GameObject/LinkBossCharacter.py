#Imports
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.GameObject.WeaponDrop import WeaponDrop
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.GameObject.Projectiles import Projectile
import me.samfreeman.GameControl.GV as GV
from random import *

from me.samfreeman.Helper.Vector import Vector


class LinkBossCharacter(BasicEnemy):

    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite("")):
        self.weapon = Sprite("images/interactive-sprites/player/DiamondSword.png")

        BasicEnemy.__init__(self,position,0,player,runLeft,runRight, True, self.weapon)
        self.damage = 0
        self.MAXIMUM_PROJECTILES = 2

        # self.weaponDrop = WeaponDrop(
        #     Vector((self.position.x, self.position.y - self.dimensions[1])),
        #     Sprite("images/interactive-sprites/player/DiamondSword.png"),
        #     Sprite("images/interactive-sprites/player/Player_UnlockingDiamond.png", 2, 10),
        #     player.state, player.frame, "The Diamond Sword"
        # )

    def move(self):
        if(self.position.x>GV.CANVAS_WIDTH):
            self.position.x = GV.CANVAS_WIDTH -100
            self.velocity.x *= -1
        BasicEnemy.move(self)

    def moveToPlayer(self):
        currentPPos = self.player.position
        self.dx = currentPPos.x - self.position.x
        BasicEnemy.moveToPlayer(self)
        if randint(0,10)  == 1:
            self.damage=3
            if abs(self.dx) < 100:
                self.attack()
            elif (self.direction ==  (self.player.directionState +1)%2):
                self.rangedAttack()
        else:
            self.damage =0

    #melee attack
    def attack(self):
        if(self.dx < 0 ):
            self.sprite = Sprite("images/interactive-sprites/link/link-attack-left.png",1,4)
        else:
            self.sprite = Sprite("images/interactive-sprites/link/link-attack-right.png",1,4)

    #rangedAttack
    def rangedAttack(self):
        SPEED = 0.4
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        #selecting the direction to send it
        if(self.dx<0):
            direction =GV.LEFT
            sprite = Sprite("images/interactive-sprites/link/link-arrow-left.png")
        else:
            direction =GV.RIGHT
            sprite = Sprite("images/interactive-sprites/link/link-arrow-right.png")
        self.projectiles.append(Projectile(self.position.copy(), 300, direction, sprite, SPEED))

    def draw(self, canvas, colour):
        BasicEnemy.draw(self, canvas, colour)
