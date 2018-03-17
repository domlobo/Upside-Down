class State:

    def __init__(self):
        self.mainMenu = True
        self.cutScene = False
        self.inLevel = False
        self.levelText = False
        self.levelPlay = False
        self.weaponPickUp = False
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
            self.inLevel = True

    def textToPlay(self):
        if self.levelText:
            self.levelText = False
            self.levelPlay = True

    def playToText(self):
        # When a new level in same stage is made -- may not need as handled by level loader
        if self.levelPlay:
            self.levelPlay = False
            self.levelText = True

    def playToCutScene(self):
        if self.inLevel:
            self.levelPlay = False
            self.inLevel = False
            self.cutScene = True

    def playToWeapon(self):
        if self.inLevel:
            self.levelPlay = False
            # self.inLevel = False
            self.weaponPickUp = True

    def weaponToCutScene(self):
        if self.weaponPickUp:
            self.inLevel = False
            self.weaponPickUp = False
            self.cutScene = True

    def gameToDeath(self):
        if self.levelPlay:
            self.levelPlay = False
            self.inLevel = False
            self.death = True

    def deathToGameOver(self):
        if self.death:
            self.death = False
            self.gameOver = True

    def gameOverToLevel(self):
        if self.gameOver:
            self.gameOver = False
            self.inLevel = True
            self.levelText = True
