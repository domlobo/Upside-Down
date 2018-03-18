#Imports
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.GameObject.Projectiles import Projectile
import me.samfreeman.GameControl.GV as GV
from random import *


class LinkBossCharacter(BasicEnemy):

    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite(""), weapon=Sprite(""), attackLeft = Sprite(""), attackRight=Sprite(""),projLeft = Sprite(""), projRight = Sprite("") ):
        self.weapon = weapon

        BasicEnemy.__init__(self,position,health,player,runLeft,runRight, True, self.weapon)
        self.damage = 0
        self.MAXIMUM_PROJECTILES = 2

        self.attackLeft = attackLeft
        self.attackRight = attackRight

        self.projLeft = projLeft
        self.projRight = projRight

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
            self.sprite = self.attackLeft
        else:
            self.sprite = self.attackLeft

    #rangedAttack
    def rangedAttack(self):
        SPEED = 0.4
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        #selecting the direction to send it
        if(self.dx<0):
            direction =GV.LEFT
            sprite = self.projLeft
        else:
            direction =GV.RIGHT
            sprite = self.projRight
        self.projectiles.append(Projectile(self.position.copy(), 300, direction, sprite, SPEED))

    def draw(self, canvas, colour):
        BasicEnemy.draw(self, canvas, colour)
