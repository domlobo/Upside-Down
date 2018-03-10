#Imports
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.GameObject.Projectiles import Projectile
from random import *

class LinkBossCharacter(BasicEnemy):

    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite("")):
        BasicEnemy.__init__(self,position,health,player,runLeft,runRight)
        self.damage = 0
        self.MAXIMUM_PROJECTILES =  2

    def moveToPlayer(self):
        currentPPos = self.player.position
        self.dx = currentPPos.x - self.position.x
        BasicEnemy.moveToPlayer(self)
        if randint(0,5)  == 1:
            self.damage=5
            if abs(self.dx) < 100:
                self.attack()
            else:
                self.rangedAttack()
        else:
            self.damage =0

    #melee attack
    def attack(self):
        if(self.dx < 0 ):
            self.sprite = Sprite("images/interactive-sprites/link/link-attack-left.png",True,1,4)
        else:
            self.sprite = Sprite("images/interactive-sprites/link/link-attack-right.png",True,1,4)

    #rangedAttack
    def rangedAttack(self):
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        #selecting the direction to send it
        if(self.dx<0):
            direction =1
        else:
            direction =2
        self.projectiles.append(Projectile(self.position.copy(), 300, direction,1.4))
