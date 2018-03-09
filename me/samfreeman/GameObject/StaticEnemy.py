# Import
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.GameObject.GameObject import GameObject
#from me.samfreeman.Helper.Rectangle import Rectangle
from me.samfreeman.Helper.Sprite import Sprite

class StaticEnemy(GameObject):

    def __init__(self, position, health, player, spriteInput=Sprite("")):
        dims = [30,60]
        if spriteInput.loaded:
            dims = [spriteInput.frameWidth, spriteInput.frameHeight]

        GameObject.__init__(self, position, Vector((0, 0)),dims , health)
        self.player = player
        self.sprite= spriteInput

    def update(self):
        GameObject.update(self)

    def draw(self, canvas, colour):
        GameObject.draw(self, canvas, colour)
        self.sprite.animate(10)
