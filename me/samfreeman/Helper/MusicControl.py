import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class MusicControl:
    def __init__(self):
        self.musicIndex = 0

        # Main Menu
        menu = simplegui._load_local_sound("Music/")

        # Stages
        stageLink = simplegui._load_local_sound("Music/")
        stageMario = simplegui._load_local_sound("Music/")
        stageDoom = simplegui._load_local_sound("Music/")


        # Cutscenes
        menuToLink = simplegui._load_local_sound("Music/")
        linkToMario = simplegui._load_local_sound("Music/")
        marioToDoom = simplegui._load_local_sound("Music/")

        # Boss Battles
        bossLink = simplegui._load_local_sound("Music/")
        bossMario = simplegui._load_local_sound("Music/")
        bossDoom = simplegui._load_local_sound("Music/")

        # WK
        stageWK = simplegui._load_local_sound("Music/")

        self.musicArray = [menu, menuToLink, stageLink, bossLink,
                           linkToMario, stageMario, bossMario,
                           marioToDoom, stageDoom, bossDoom]
        self.currentMusic = self.musicArray[self.musicIndex]

    def playCurrentMusic(self):
        self.currentMusic.play()
    def stopCurrentMusic(self):
        self.currentMusic.pause()

    def nextSong(self):
        self.stopCurrentMusic()
        self.musicIndex += 1
        self.currentMusic = self.musicArray[self.musicIndex]
        self.playCurrentMusic()