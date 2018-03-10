# Import
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.GameObject.GameObject import GameObject
from me.samfreeman.Helper.Sprite import Sprite
import me.samfreeman.GameControl.GV as GV

class StaticEnemy(GameObject):

    def __init__(self, position, health, player, spriteInput=Sprite("")):
        dims = [30,60]
        if spriteInput.loaded:
            dims = [spriteInput.frameWidth, spriteInput.frameHeight]

        GameObject.__init__(self, position, Vector((0, 0)),dims , health)
        self.player = player
        self.sprite= spriteInput
        self.damage = 0.5
        self.projectiles = []

    def update(self):
        GameObject.update(self)
        # Projectiles
        for proj in self.projectiles[:]:
            proj.update()
            if proj.position.x <=0  or proj.position.x >= GV.CANVAS_WIDTH:
                proj.remove = True
            if proj.remove: self.projectiles.remove(proj)

    def draw(self, canvas, colour):
        GameObject.draw(self, canvas, colour)
        self.sprite.animate(10)
