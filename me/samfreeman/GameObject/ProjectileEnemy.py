from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.GameObject.Projectiles import Projectile
import me.samfreeman.GameControl.GV as GV
from random import *
class ProjectileEnemy(BasicEnemy):

    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite(""), leftShoot=Sprite(""), rightShoot=Sprite("")):
        BasicEnemy.__init__(self, position, health, player, runLeft, runRight)
        self.leftShoot = leftShoot
        self.rightShoot = rightShoot

        self.MAXIMUM_PROJECTILES = 3
        self.CHANCE_TO_FIRE = 3
        self.coinValue =1

    def moveToPlayer(self):
        BasicEnemy.moveToPlayer(self)
        self.dx = self.player.position.x - self.position.x

        if (randint(0,self.CHANCE_TO_FIRE)  == 1) and (self.direction ==  (self.player.directionState +1)%2):
            self.rangedAttack()

    def rangedAttack(self):
        SPEED = 0.7
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        #selecting the direction to send it
        if(self.dx<0):
            direction =GV.LEFT
            sprite = self.leftShoot
        else:
            direction =GV.RIGHT
            sprite =self.rightShoot
        self.projectiles.append(Projectile(self.position.copy(), 300, direction, sprite, SPEED))
