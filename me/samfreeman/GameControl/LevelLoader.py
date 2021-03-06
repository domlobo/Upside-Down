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

    def __init__(self,player,inter, state):
        self.player = player
        self.inter = inter
        self.state = state

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
            "", #no background
            "images/background/link/link-boss-stage.png",
            cloudsURL,player,inter, "Tutorial-3")

        marioOne = Level("images/background/mario/hills.png",
                         "images/background/mario/Mario-world-1.1.png",
                         cloudsURL,player,inter, "Mario-1")

        marioTwo = Level("images/background/mario/hills.png",
                         "images/background/mario/Mario-world-1.1.png",
                         cloudsURL,player,inter, "Mario-2")
        marioThree = Level("",#no background
                         "images/background/mario/mario-boss-level.png",
                         cloudsURL,player,inter, "Mario-3")

        doomOne = Level("images/background/doom/base-layer-background.jpg",
                        "images/background/doom/second layer.png",
                         "", player,inter,"Doom-1")
        doomTwo = Level("images/background/doom/base-layer-background.jpg",
                        "images/background/doom/second layer.png",
                         "", player,inter,"Doom-2")
        doomThree = Level("images/background/doom/boss_background.jpg",
                        "images/background/doom/second layer.png",
                         "", player,inter,"Doom-3")

        lastLevel = Level("", "images/background/pokemon/pikachu/pikachu-stage.png",
                          cloudsURL, player, inter, "Death")

        # Creating list of levels

        self.levels =[tutorialOne,tutorialTwo,tutorialThree,marioOne,marioTwo,marioThree,doomOne,doomTwo,doomThree, lastLevel]
        self.enemyFiles =("enemies/tutorialOne.txt","enemies/tutorialTwo.txt","enemies/tutorialThree.txt","enemies/marioOne.txt","enemies/marioTwo.txt","enemies/marioThree.txt","enemies/doomOne.txt", "enemies/doomTwo.txt", "enemies/doomThree.txt", "enemies/lastLevel.txt")


        self.levelCounter=0
        self.currentLevel=self.levels[self.levelCounter]
        self.currentLevel.loadLevelSpecifics(self.enemyFiles[self.levelCounter])
        self.player.numberOfDeaths = 0
    #called from Game when a level is over
    def nextlevel(self):
        self.player = self.currentLevel.returnPlayer()
        self.player.position.x = 50
        self.player.position.y = GV.CANVAS_HEIGHT/2
        self.player.health = 100

        self.state.playToText()

        if(len(self.levels)>0):
            self.levelCounter +=1
            #reset the death counter after each stage (every 3 levels)

            del self.levels[0]
            self.currentLevel = self.levels[0]
            self.currentLevel.setPlayer(self.player)
            self.currentLevel.loadLevelSpecifics(self.enemyFiles[self.levelCounter])
            #stops the character sticking to the right hand side after the transition
            GameObject.update(self.currentLevel.player)
            if (self.levelCounter + 1) % 3 == 0:
                # Boss Battle
                self.state.boss()

            if (self.levelCounter % 3 == 0):
                self.player.numberOfDeaths = 0
                self.player.maxUnlockedWeapon += 1
                self.state.playToCutScene()
            if self.levelCounter > 9: GV.on_last = True

    def gameOver(self):
        #three retries
        self.currentLevel.enemies = []
        self.currentLevel.objects = []
        if(self.player.numberOfDeaths <3):
            #go back to the start of the level
            self.player.numberOfDeaths +=1
            self.state.gameOverToLevel()
        else:
            self.state.gameOverToScore()
            self.player.numberOfDeaths=0
        #start level
        self.player.health = 100
        self.player.position.x = 50
        self.player.position.y = GV.CANVAS_HEIGHT/2
        self.player.attackingSword = False
        self.currentLevel.background.farBackgroundPos = Vector((self.currentLevel.background.FAR_BACKGROUND_WIDTH / 2, GV.CANVAS_HEIGHT / 2))
        self.currentLevel.background.foregroundPos = Vector((self.currentLevel.background.FOREGROUND_WIDTH / 2, GV.CANVAS_HEIGHT / 2))
        self.currentLevel.loadLevelSpecifics(self.enemyFiles[self.levelCounter])
        GameObject.update(self.currentLevel.player)
