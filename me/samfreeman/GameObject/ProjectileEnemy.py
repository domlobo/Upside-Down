from me.samfreeman.GameObject.Enemy import BasicEnemy
from me.samfreeman.Helper.Sprite import Sprite
import me.samfreeman.GameControl.GV as GV
class ProjectileEnemy(BasicEnemy):

    def __init__(self, position, health, player, runLeft=Sprite(""), runRight=Sprite(""), leftShoot=Sprite(""), rightShoot=Sprite("")):
        Enemy.init(self, position, health, player, runLeft=Sprite(""), runRight=Sprite(""))
        self.leftShoot = leftShoot
        self.rightShoot = rightShoot

        self.MAXIMUM_PROJECTILES = 3
        self.CHANCE_TO_FIRE = 3

    def moveToPlayer(self):
        Enemy.moveToPlayer(self)
        self.dx = self.player.position.x - self.position.x

        if randint(0,CHANCE_TO_FIRE)  == 1:
            self.rangedAttack()

    def rangedAttackI(self):
        SPEED = 0.7
        if len(self.projectiles) == self.MAXIMUM_PROJECTILES: return
        #selecting the direction to send it
        if(self.dx<0):
            direction =GV.LEFT
            sprite = leftShoot
        else:
            direction =GV.RIGHT
            sprite = rightShoot
        self.projectiles.append(Projectile(self.position.copy(), 300, direction, sprite, SPEED))
