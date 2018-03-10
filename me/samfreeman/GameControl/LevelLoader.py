try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from ..GameObject.GameObject import GameObject
from ..Levels.Level import Level
from me.samfreeman.Helper.TextOverlay import TextOverlay
from me.samfreeman.Helper.Vector import Vector
import me.samfreeman.GameControl.GV as GV


class LevelLoader:

    def __init__(self,player,inter):
        self.player = player
        self.inter = inter
        #setting up levels
        cloudsURL = "images/background/mario/Mario-world-clouds.png"
        #tutorial (zelda) levels
        tutorialOne = Level(
            "images/background/link/link-background.jpg",
            "images/background/link/link-tutorial-world-1.png",
            cloudsURL,player,inter, "Tutorial-1")
        tutorialTwo = Level(
            "images/background/link/link-background.jpg",
            "images/background/link/link-tutorial-world-2.png",
            cloudsURL,player,inter, "Tutorial-2")
        tutorialThree = Level(
            "images/background/link/link-background.jpg",
            "images/background/link/link-tutorial-world.png",
            cloudsURL,player,inter, "Tutorial-3")

        marioOne = Level("images/background/mario/hills.png",
                         "images/background/mario/Mario-world-1.1.png",
                         cloudsURL,player,inter, "Mario-1")

        doomOne = Level("images/background/doom/base-layer-background.jpg",
                        "images/background/doom/second layer.png",
                         "", player,inter,"Doom-1")
        # Creating list of levels
        self.levels =(doomOne,)#(tutorialOne,tutorialTwo,tutorialThree,marioOne,doomOne)
        self.enemyFiles =("enemies/doomOne.txt",)#("enemies/tutorialOne.txt","enemies/tutorialTwo.txt","enemies/tutorialThree.txt","enemies/marioOne.txt","enemies/doomOne.txt")
        # Selecting the first level
        self.levelCounter=0
        self.currentLevel=self.levels[self.levelCounter]
        self.currentLevel.loadLevelSpecifics(self.enemyFiles[self.levelCounter])
        self.numberOfDeaths = 0
    #called from Game when a level is over
    def nextlevel(self):
        self.player = self.currentLevel.returnPlayer()
        self.player.position.x = 0
        self.player.health = 100

        if(self.levelCounter<len(self.levels)-1):
            self.levelCounter +=1
            #reset the death counter after each stage (every 3 levels)
            if(self.levelCounter%3 == 0):
                self.numberOfDeaths =0
            self.currentLevel = self.levels[self.levelCounter]
            self.currentLevel.setPlayer(self.player)
            self.currentLevel.loadLevelSpecifics(self.enemyFiles[self.levelCounter])
            #stops the character sticking to the right hand side after the transition
            GameObject.update(self.currentLevel.player)

    def gameOver(self):
        #three retries outside of the first two tutorial levels
        if(self.numberOfDeaths <3 or self.levelCounter<2):
            self.player.health = 100
            #go back to the start of the level
            self.player.position.x = 0
            self.currentLevel.enemies = []
            self.currentLevel.objects = []
            self.currentLevel.background.farBackgroundPos = Vector((self.currentLevel.background.FAR_BACKGROUND_WIDTH / 2, GV.CANVAS_HEIGHT / 2))
            self.currentLevel.background.foregroundPos = Vector((self.currentLevel.background.FOREGROUND_WIDTH / 2, GV.CANVAS_HEIGHT / 2))
            self.currentLevel.loadLevelSpecifics(self.enemyFiles[self.levelCounter])
            GameObject.update(self.currentLevel.player)
        else:
            exit()
