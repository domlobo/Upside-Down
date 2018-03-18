import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class MusicControl:
    def __init__(self):
        self.musicIndex = 0

        # Main Menu
        menu = simplegui._load_local_sound("Music/menu.ogg")

        # Stages
        stageLink = simplegui._load_local_sound("Music/stageLink.ogg")
        stageMario = simplegui._load_local_sound("Music/stageMario.ogg")
        stageDoom = simplegui._load_local_sound("Music/stageDoom.ogg")


        # Cutscenes
        menuToLink = simplegui._load_local_sound("Music/menuToLink.ogg")
        linkToMario = simplegui._load_local_sound("Music/linkToMario.ogg")
        marioToDoom = simplegui._load_local_sound("Music/marioToDoom.ogg")

        # Boss Battles
        bossLink = simplegui._load_local_sound("Music/bossLink.ogg")
        bossMario = simplegui._load_local_sound("Music/bossMario.ogg")
        bossDoom = simplegui._load_local_sound("Music/bossDoom.ogg")

        # WK
        wk = simplegui._load_local_sound("Music/wk.ogg")

        self.musicArray = [menu, menuToLink, stageLink, bossLink,
                           linkToMario, stageMario, bossMario,
                           marioToDoom, stageDoom, bossDoom, wk]
        self.currentMusic = self.musicArray[self.musicIndex]

    def nextSong(self):
        self.currentMusic.pause()
        self.musicIndex += 1
        self.currentMusic = self.musicArray[self.musicIndex]
        self.currentMusic.play()