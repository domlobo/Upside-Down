#Imports
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.GameObject.FireBalls import FireBall
import me.samfreeman.GameControl.GV as GV
from random import *

class MarioBossCharacter(BasicEnemy):
    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite("")):
        self.weapon = Sprite("images/interactive-sprites/player/Fireball.png")

        BasicEnemy.__init__(self,position,health,player,runLeft,runRight, True, self.weapon)
        self.damage = 0
        self.fireballs = []
        self.MAXIMUM_FIREBALLS = 3

    def update(self):
        BasicEnemy.update(self)
        for fball in self.fireballs[:]:
            if fball.remove:
                self.fireballs.remove(fball)
                continue
            fball.update()


    def move(self):
        if(self.position.x>GV.CANVAS_WIDTH):
            self.position.x = GV.CANVAS_WIDTH -20
            self.velocity.x *= -1
        elif(self.position.x<=0):
            self.position.x = 20
            self.velocity.x *=-1
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
            self.sprite = Sprite("images/interactive-sprites/mario/mario-ultimate-left.png",1,7,True)
        else:
            self.sprite = Sprite("images/interactive-sprites/mario/mario-ultimate-right.png",1,7,True)

    #rangedAttack
    def rangedAttack(self):
        SPEED = 0.4
        if len(self.projectiles) == self.MAXIMUM_FIREBALLS: return
        #selecting the direction to send it
        if(self.dx<0):
            direction =GV.LEFT
        else:
            direction =GV.RIGHT
        self.fireballs.append(FireBall(self.position.copy(), self.velocity.copy(), direction, self.dimensions[0] / 2, 5))
