try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from me.samfreeman.Input.Keyboard import Keyboard

class Interaction:

    def __init__(self, player):
        self.keyboard = Keyboard()
        self.player = player

    # handling keyboard input for player
    def checkKeyboard(self):
        if self.keyboard.right:
            self.player.moveRight()
        if self.keyboard.left:
            self.player.moveLeft()
        if self.keyboard.up:
            self.player.jump()
        if self.keyboard.down:
            self.player.crouch()

        if not (self.keyboard.down or self.keyboard.right or self.keyboard.left or self.player.attackingSword):
            self.player.stand()

        # if (not(self.keyboard.right and self.keyboard.left)) and (self.player.direction != 0):
        #     self.player.standStill()

        # if (self.keyboard.weapon != self.player.weapon):
        #     self.player.tryWeapon(self.keyboard.weapon)

    def clickHandler(self,pos):
       # self.player.shoot()
        self.player.swordAttack()

    def checkProjectileCollision(self,enemies,player):
        # Using a copy to remove from actual list if there is too much health loss
        for enemy in enemies[:]:
            for proj in player.projectiles[:]:
                if enemy.boundingBox.overlaps(proj.boundingBox):
                    # Collision
                    enemy.changeHealth(-proj.damage)
                    proj.remove = True
            if enemy.remove: enemies.remove(enemy)

    def checkObjectCollision(self,objects,player):
        # Using a copy to remove from actual list if there is too much health loss
        for currentObject in objects[:]:
            if currentObject.boundingBox.overlaps(player.boundingBox):
                print("collision")
