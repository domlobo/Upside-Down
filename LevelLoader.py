try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Level import Level

class LevelLoader:

    def __init__(self,player,inter):
        self.player = player
        self.inter = inter
        tutorialOne = Level('','https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/link/link-tutorial-world.jpg?token=APgKaYNg0cYs3Pz7tg6Yk1TWGxuLV6Egks5aoa9MwA%3D%3D','https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-clouds.png?token=APgKaSIkI0DepOY41ozT1p6k03q-8_-vks5aoT75wA%3D%3D',player,inter)
        self.levels = (tutorialOne,Level('https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/hills.png?token=APgKaX34fYs3AdO_hIuWXG7_M_m2FNK7ks5aoZucwA%3D%3D','https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-1.1.png?token=APgKaRDpvbFC1-I2_-idKugD_sm8BXH-ks5aoaAswA%3D%3D',
        'https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-clouds.png?token=APgKaSIkI0DepOY41ozT1p6k03q-8_-vks5aoT75wA%3D%3D',
         player,inter))
        self.levelCounter=0
        self.currentLevel=self.levels[self.levelCounter]

    #called from Game when a level is over
    def nextlevel(self):
        self.player = self.currentLevel.returnPlayer()
        self.player.position.x = 0
        if(self.levelCounter<len(self.levels)-1):
            self.levelCounter +=1
            self.currentLevel = self.levels[self.levelCounter]
            self.currentLevel.setPlayer(self.player)
