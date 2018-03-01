# imports
from Player import Player
from Enemy import BasicEnemy


class PlayerEnemyInteraction:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def checkProjectileCollision(self):
        # Using a copy to remove from actual list if there is too much health loss
        for enemy in self.enemies[:]:
            for proj in self.player.projectiles[:]:
                if enemy.boundingBox.overlaps(proj.boundingBox):
                    # Collision
                    enemy.changeHealth(-proj.damage)
                    proj.remove = True
            if enemy.remove: self.enemies.remove(enemy)

    def update(self):
        self.checkProjectileCollision()