from me.samfreeman.GameControl import GV
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.Helper.Vector import Vector


class Wife(GameObject):
    def __init__(self, position, health, player, spriteInput=Sprite("")):
        dims = [30, 60]
        if spriteInput.hasPath:
            dims = [90, 90]

        GameObject.__init__(self, position, Vector((0, 0)), dims, health)

        self.wife = True
        self.shot = False
        self.dyingSprite = Sprite("images/cutscenes/Wife_Dying_Left.png", 6, 6, True)
        self.player = player
        self.sprite = spriteInput
        self.damage = 0.5
        self.boss = False
        self.projectiles = []
        self.coinValue = 1

    def draw(self, canvas, colour):
        print(GV.win)
        GameObject.draw(self, canvas, colour)
        if GV.win:
            self.sprite = self.dyingSprite
            self.sprite.startAnimation(8, True)
            if self.sprite.isComplete:
                # THIS IS WHERE RESET GOES
        else: self.sprite.startAnimation(8)

    def dropCoin(self, size, cost):
        pass

    def update(self):
        GameObject.update(self)

    def resetMovement(self):
        #required method for the update for loop in Level
        pass

