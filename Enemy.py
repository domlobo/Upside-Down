#imports
from GameObject import GameObject
from Vector import Vector

class BasicEnemy(GameObject):
    def __init__(self, position, health, player):
        GameObject.__init__(self, position, Vector((0, 0)), [30, 60], health)
        self.player = player
        self.direction = 0

        self.maxVel = [3, 3]

    def caclulatePlayerPosition(self):
        currentPPos = self.player.position.getP()
        self.velocity.add(Vector())