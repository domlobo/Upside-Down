try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Keyboard import Keyboard

class Interaction:

    def __init__(self, player):
        self.keyboard = Keyboard()
        self.player = player

    #handling keyboard input for player
    def checkKeyboard(self):
        if (self.keyboard.right):
            player.moveRight()
        if (self.keyboard.left):
            player.moveLeft()
        if (self.keyboard.up):
            player.jump()
        if (self.keyboard.down):
            player.crouch()
        if (not(self.keyboard.right and self.keyboard.left)) and (player.direction != 0):
            player.standStill()

        if (self.keyboard.weapon != player.weapon):
            player.tryWeapon(self.keyboard.weapon)

    def clickHandler(self,pos):
        player.fire()
