class State:

    def __init__(self):
        self.mainMenu = True
        self.cutScene = False
        self.levelText = False
        self.levelPlay = False
        self.bossText = False
        self.bossPlay = False
        self.death = False
        self.gameOver = False

    def menuToCutScene(self):
        if self.mainMenu:
            self.mainMenu = False
            self.cutScene = True

    def cutSceneToLevel(self):
        if self.cutScene:
            self.cutScene = False
            self.levelText = True

    def textToPlay(self):
        if self.levelText:
            self.levelText = False
            self.levelPlay = True

    def playToText(self):
        # When a new level in same stage is made -- may not need as handled by level loader
        if self.levelPlay:
            self.levelPlay = False
            self.levelText = True

    def playToBoss(self):
        if self.levelPlay:
            self.levelPlay = False
            self.bossText = True

    def bossTextToPlay(self):
        if self.bossText:
            self.bossText = False
            self.bossPlay = True

    def bossToCutScene(self):
        if self.bossPlay:
            self.bossPlay = False
            self.cutScene = True

    def death(self):
        if self.levelPlay or self.bossPlay:
            self.levelPlay = False
            self.bossPlay = False
            self.death = True

    def deathToGameOver(self):
        if self.death:
            self.death = False
            self.gameOver = True
