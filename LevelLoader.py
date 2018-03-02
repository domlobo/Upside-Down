try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Level import Level
from GameObject import GameObject

class LevelLoader:

    def __init__(self,player,inter):
        self.player = player
        self.inter = inter
        tutorialOne = Level("","images/background/link/link-tutorial-world.jpg","images/background/mario/Mario-world-clouds.png",player,inter)
        self.levels = (tutorialOne,Level("images/background/mario/hills.png","images/background/mario/Mario-world-1.1.png","images/background/mario/Mario-world-clouds.png",player,inter))
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
            #stops the character sticking to the right hand side after the transition
            GameObject.update(self.currentLevel.player)
