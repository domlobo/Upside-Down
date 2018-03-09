try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from me.samfreeman.Input.Keyboard import Keyboard

class Interaction:

    def __init__(self, player, text):
        self.keyboard = Keyboard()
        self.player = player
        self.text = text #----> used for testing purposes

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
        if self.keyboard.j:
            self.player.swordAttack() # TODO: UPDATE SO THAT IT SELECTS THE CURRENT ATTACK - GUN OR SWORD
        if self.keyboard.k:
            self.player.fireballAttack()
        if self.keyboard.enter:
            self.text.nextText()
            self.keyboard.enter=False

        if not (self.keyboard.down or self.keyboard.right or self.keyboard.left or self.player.attackingSword):
            self.player.stand()

        # if (not(self.keyboard.right and self.keyboard.left)) and (self.player.direction != 0):
        #     self.player.standStill()

        # if (self.keyboard.weapon != self.player.weapon):
        #     self.player.tryWeapon(self.keyboard.weapon)


    def checkProjectileCollision(self,enemies,player):
        # Using a copy to remove from actual list if there is too much health loss
        for enemy in enemies[:]:
            if player.boundingBox.overlaps(enemy.boundingBox):
                player.changeHealth(-0.5)
            for proj in player.projectiles[:]:
                if enemy.boundingBox.overlaps(proj.boundingBox):
                    # Collision
                    enemy.changeHealth(-proj.damage)
                    proj.remove = True
            for fball in player.fireballs[:]:
                if enemy.boundingBox.overlaps(fball.boundingBox):
                    # Collision
                    enemy.changeHealth(-fball.damage)
                    fball.remove = True
            if player.swordBoundingBox.overlaps(enemy.boundingBox):
                print("BANG__!_!_!_!_!_!_!_!_!_!_!_!_")
                enemy.changeHealth(-player.swordDamage)
            if enemy.remove: enemies.remove(enemy)

    def checkObjectCollision(self,objects,entity):
        # Using a copy to remove from actual list if there is too much health loss
        #can move booleans
        entity.canMoveLeft = True
        entity.canMoveRight = True
        entity.canMoveUp = True
        entity.canMoveDown = True
        # self.player.currentGround = 470 + self.player.dimensions[1] / 2
        for currentObject in objects[:]:
            if currentObject.boundingBox.overlaps(entity.boundingBox):
                if entity.boundingBox.bottom > currentObject.boundingBox.top and(entity.position.x <= currentObject.boundingBox.right and entity.position.x >= currentObject.boundingBox.left and entity.position.y <= currentObject.boundingBox.top):
                    entity.canMoveDown = False
                    # self.player.onGround = False
                    self.player.hasJumped = False
                    # self.player.currentGround = currentObject.boundingBox.top
                if (entity.boundingBox.right > currentObject.boundingBox.left) and (entity.position.x < currentObject.position.x) and (entity.position.y <= currentObject.boundingBox.bottom and entity.position.y >= currentObject.boundingBox.top):
                    entity.canMoveRight = False
                    entity.velocity.x *= -1
                if (entity.boundingBox.left < currentObject.boundingBox.right) and (entity.position.x > currentObject.position.x) and (entity.position.y <= currentObject.boundingBox.bottom and entity.position.y >= currentObject.boundingBox.top):
                    entity.canMoveLeft = False
                    entity.velocity.x *= -1
                if entity.boundingBox.top < currentObject.boundingBox.bottom and(entity.position.x <= currentObject.boundingBox.right and entity.position.x >= currentObject.boundingBox.left and entity.position.y >= currentObject.boundingBox.bottom):
                    entity.canMoveUp = False
                    entity.velocity.y *= -1
