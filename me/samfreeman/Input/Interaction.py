from me.samfreeman.GameControl import GV

try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from me.samfreeman.Input.Keyboard import Keyboard
from me.samfreeman.GameObject.FireBalls import FireBall

keyboard = Keyboard()

class Interaction:

    def __init__(self, player, text, cs, state, unlocks):
        self.keyboard = keyboard
        self.player = player
        self.text = text #----> used for testing purposes
        self.cs = cs
        self.state = state
        self.unlocks = unlocks
        self.justCrouched=False

    # handling keyboard input for player
    def checkKeyboard(self):
        if self.state.inLevel:
            if self.state.levelPlay:
                # Means no running an shooting
                if not self.player.attackingSword or self.player.attackingFire:
                    if self.keyboard.right:
                        self.player.moveRight()
                    if self.keyboard.left:
                        self.player.moveLeft()
                    if self.keyboard.up:
                        self.player.jump()
                    if self.keyboard.down:
                        self.player.crouch()
                        self.justCrouched = True
                if self.keyboard.j and not self.player.hasJumped and not self.player.attackingFire: # This prevents a bug that breaks the player if they swing in the air -- may come back and fix
                    self.player.swordAttack()
                if self.keyboard.k and (self.player.maxUnlockedWeapon >1) and not self.player.attackingSword:
                    self.player.fireballAttack()
                if self.keyboard.l and self.player.maxUnlockedWeapon >2:
                    self.player.shoot()
                if self.keyboard.b:
                    GV.bounding_box = not GV.bounding_box
            else:
                if self.keyboard.q:
                    self.text.nextText()
                    if self.text.done:
                        self.state.textToPlay()
                    self.keyboard.q=False

            if not (self.keyboard.down or self.keyboard.right or self.keyboard.left or self.player.attackingSword or self.player.hasJumped):
                self.player.stand()
                if self.justCrouched:
                    self.justCrouched = False
                    self.player.checkPosition = True

        elif self.state.cutScene:
            if self.keyboard.q:
                self.cs[0].nextLine()
                self.keyboard.q=False
            if self.keyboard.up:
                pass

        elif self.state.mainMenu:
            if self.keyboard.up:
                self.state.menuToCutScene()
                # self.state.cutSceneToLevel()

        elif self.state.weaponPickUp:
            if self.keyboard.q:
                self.unlocks.counter += 1
                self.unlocks.hasUpdated = True
                self.state.weaponToLevel()
                self.keyboard.q = False

        elif self.state.score:
            if self.keyboard.q:
                GV.need_reset = True
                self.state.scoreToMenu()

    def checkProjectileCollision(self,enemies,player):
        # Using a copy to remove from actual list if there is too much health loss
        damageDealtSword = False
        damageDealtJump = False
        for enemy in enemies[:]:
            #player collision damage
            if player.boundingBox.overlaps(enemy.boundingBox):
                player.changeHealth(-enemy.damage)
                player.displayHit()
            #gun damage
            for proj in player.projectiles[:]:
                if enemy.boundingBox.overlaps(proj.boundingBox):
                    # Collision
                    enemy.changeHealth(-proj.damage)
                    proj.remove = True
            for proj in enemy.projectiles[:]:
                if player.boundingBox.overlaps(proj.boundingBox):
                    # Collision
                    player.changeHealth(-proj.damage)
                    player.displayHit()
                    proj.remove = True
            #fireball damage
            for fball in player.fireballs[:]:
                if enemy.boundingBox.overlaps(fball.boundingBox):
                    # Collision
                    enemy.changeHealth(-fball.damage)
                    fball.remove = True
            #fireball damage for player
            if hasattr(enemy,'fireballs'):
                for fball in enemy.fireballs[:]:
                    if player.boundingBox.overlaps(fball.boundingBox):
                        player.changeHealth(-fball.damage)
                        fball.remove = True
            #sword damage
            if player.swordBoundingBox.overlaps(enemy.boundingBox) and not(player.swordHit):
                enemy.changeHealth(-player.swordDamage)
                damageDealtSword = True
            #jumping on enemy damage
            if enemy.boundingBox.top < player.boundingBox.bottom and(enemy.position.x <= player.boundingBox.right and enemy.position.x >= player.boundingBox.left and enemy.position.y >= player.boundingBox.bottom) and not(player.jumpHit):
                enemy.changeHealth(-50)
                damageDealtJump = True
            if enemy.remove: enemies.remove(enemy)
            #stop enemy walking through player
            if (enemy.boundingBox.right > player.boundingBox.left) and (enemy.position.x < player.position.x) and (enemy.position.y <= player.boundingBox.bottom and enemy.position.y >= player.boundingBox.top):
                enemy.canMoveRight = False
                enemy.velocity.x *= -1
            if (enemy.boundingBox.left < player.boundingBox.right) and (enemy.position.x > player.position.x) and (enemy.position.y <= player.boundingBox.bottom and enemy.position.y >= player.boundingBox.top):
                enemy.canMoveLeft = False
                enemy.velocity.x *= -1

        #means that damage can be dealt to multiple enemies in one swing
        if damageDealtSword:
            #only deal damage once per swing
            player.swordHit = True
            damageDealtSword = False
        if damageDealtJump:
            player.jumpHit = True
            damageDealtJump = False

    def checkObjectCollision(self,objects,entity):
        # Using a copy to remove from actual list if there is too much health loss
        #can move booleans
        entity.canMoveLeft = True
        entity.canMoveRight = True
        entity.canMoveUp = True
        entity.canMoveDown = True
        # self.player.currentGround = 470 + self.player.dimensions[1] / 2
        for currentObject in objects[:]:
            #if the object overlaps
            if(currentObject.notCollidable ==1) or not(currentObject.boundingBox.overlaps(entity.boundingBox)): continue
            if entity.boundingBox.bottom >= currentObject.boundingBox.top and(entity.position.x <= currentObject.boundingBox.right and entity.position.x >= currentObject.boundingBox.left and entity.position.y <= currentObject.boundingBox.top):
                entity.canMoveDown = False
                entity.hasJumped = False
                if entity == self.player:
                    entity.jumpHit = False
                #bounce fireballs and nothing else
                if type(entity) == FireBall:
                    entity.velocity.y *=-1
                else:
                    entity.velocity.y =0
                entity.currentGround = currentObject.boundingBox.top
            if (entity.boundingBox.right >= currentObject.boundingBox.left) and (entity.position.x < currentObject.position.x) and (((entity.position.y <= currentObject.boundingBox.bottom)and (entity.position.y >= currentObject.boundingBox.top)) or ((currentObject.position.y <= entity.boundingBox.bottom) and (currentObject.position.y >= entity.boundingBox.top))):
                entity.canMoveRight = False
                entity.velocity.x *= -1
            if (entity.boundingBox.left <= currentObject.boundingBox.right) and (entity.position.x > currentObject.position.x) and (((entity.position.y <= currentObject.boundingBox.bottom)and (entity.position.y >= currentObject.boundingBox.top)) or ((currentObject.position.y <= entity.boundingBox.bottom) and (currentObject.position.y >= entity.boundingBox.top))):
                entity.canMoveLeft = False
                entity.velocity.x *= -1
            if entity.boundingBox.top < currentObject.boundingBox.bottom and(entity.position.x <= currentObject.boundingBox.right and entity.position.x >= currentObject.boundingBox.left and entity.position.y >= currentObject.boundingBox.bottom):
                entity.canMoveUp = False
                #slowly bounce back
                entity.velocity.y *= -0.01
                entity.position.y = currentObject.boundingBox.bottom + (entity.dimensions[1]/2)

    def checkCollectibleCollision(self,collectibles, player):
        for collectible in collectibles[:]:
            if player.boundingBox.contains(collectible.position):
                if collectible.type == 0:
                    player.collectedCoins = collectible.pickUp(player.collectedCoins)
                else: collectible.pickUp() # for bosses
                # coins.remove(coin)
