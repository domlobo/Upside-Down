#Imports
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.GameObject.Projectiles import Projectile
import me.samfreeman.GameControl.GV as GV
from random import *

class LinkBossCharacter(BasicEnemy):

    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite("")):
        BasicEnemy.__init__(self,position,0,player,runLeft,runRight)
        self.damage = 0
        self.MAXIMUM_PROJECTILES = 2

    def moveToPlayer(self):
        print(self.position)
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
