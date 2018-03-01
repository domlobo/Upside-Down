try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Level import Level

class LevelLoader:

    def __init__(self,player,inter):
        self.player = player
        self.inter = inter
        self.levels = (Level('https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-1.1.jpg?token=APgKaY-Q3e5QVhZ-H89jyYEck_xcLGKSks5aoWDHwA%3D%3D','','https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-clouds.png?token=APgKaSIkI0DepOY41ozT1p6k03q-8_-vks5aoT75wA%3D%3D', player,inter),Level("","","",player,inter))
        self.levelCounter=-1
        self.currentLevel=self.levels[self.levelCounter]

    #called from Game when a level is over
    def nextlevel(self,frame):
        self.player = self.currentLevel.returnPlayer
        if(self.levelCounter<len(self.levels)-1):
            self.levelCounter +=1
            self.currentLevel = self.levels[self.levelCounter]
            frame.set_draw_handler(self.currentLevel.draw)
            return frame
