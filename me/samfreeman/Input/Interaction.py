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

    def checkEnemyPlayerCollision(self,enemies,player):
        # Using a copy to remove from actual list if there is too much health loss
        for enemy in enemies[:]:
            if player.boundingBox.overlaps(enemy.boundingBox):
                player.changeHealth(-0.5)
            for proj in player.projectiles[:]:
                if enemy.boundingBox.overlaps(proj.boundingBox):
                    # Collision
                    enemy.changeHealth(-proj.damage)
                    proj.remove = True
            if enemy.remove: enemies.remove(enemy)

    def checkObjectCollision(self,objects,entity):
        # Using a copy to remove from actual list if there is too much health loss
        #can move booleans
        entity.canMoveLeft = True
        entity.canMoveRight = True
        entity.canMoveUp = True
        entity.canMoveDown = True
        for currentObject in objects[:]:
            if currentObject.boundingBox.overlaps(entity.boundingBox):
                if entity.boundingBox.bottom > currentObject.boundingBox.top and(entity.position.x <= currentObject.boundingBox.right and entity.position.x >= currentObject.boundingBox.left):
                    entity.canMoveDown = False
                if (entity.boundingBox.right > currentObject.boundingBox.left) and (entity.position.x < currentObject.position.x) and (entity.position.y <= currentObject.boundingBox.bottom and entity.position.y >= currentObject.boundingBox.top):
                    entity.canMoveRight = False
                if (entity.boundingBox.left < currentObject.boundingBox.right) and (entity.position.x > currentObject.position.x) and (entity.position.y <= currentObject.boundingBox.bottom and entity.position.y >= currentObject.boundingBox.top):
                    entity.canMoveLeft = False
                if entity.boundingBox.top < currentObject.boundingBox.bottom and(entity.position.x <= currentObject.boundingBox.right and entity.position.x >= currentObject.boundingBox.left):
                    entity.canMoveUp = False
