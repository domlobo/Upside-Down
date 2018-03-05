try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from ..GameObject.GameObject import GameObject
from ..Levels.Level import Level


class LevelLoader:

    def __init__(self,player,inter):
        self.player = player
        self.inter = inter
        #setting up levels
        cloudsURL = "images/background/mario/Mario-world-clouds.png"
        #tutorial (zelda) levels
        tutorialOne = Level(
            "",
            "images/background/link/link-tutorial-world.jpg",
            cloudsURL,player,inter, "Tutorial-1")
        tutorialTwo = Level("",
                            "images/background/link/link-tutorial-world.jpg",
                            cloudsURL,player,inter, "Tutorial-2")
        tutorialThree = Level("",
                              "images/background/link/link-tutorial-world.jpg",
                              cloudsURL,player,inter, "Tutorial-3")

        marioOne = Level("images/background/mario/hills.png",
                         "images/background/mario/Mario-world-1.1.png",
                         cloudsURL,player,inter, "Mario-1")
        # Creating list of levels
        self.levels = (tutorialOne,tutorialTwo,tutorialThree,marioOne)
        self.enemyFiles =("enemies/tutorialOne.txt","enemies/tutorialTwo.txt","enemies/tutorialThree.txt","enemies/tutorialOne.txt")
        # Selecting the first level
        self.levelCounter=0
        self.currentLevel=self.levels[self.levelCounter]
        self.currentLevel.loadEnemies(self.enemyFiles[self.levelCounter])

    #called from Game when a level is over
    def nextlevel(self):
        self.player = self.currentLevel.returnPlayer()
        self.player.position.x = 0

        if(self.levelCounter<len(self.levels)-1):
            self.levelCounter +=1
            self.currentLevel = self.levels[self.levelCounter]
            self.currentLevel.setPlayer(self.player)
            self.currentLevel.loadEnemies(self.enemyFiles[self.levelCounter])
            #stops the character sticking to the right hand side after the transition
            GameObject.update(self.currentLevel.player)
