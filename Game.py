# Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameControl.LevelLoader import LevelLoader
from me.samfreeman.GameObject.Player import Player
from me.samfreeman.Helper.Cutscene import Cutscene
from me.samfreeman.Helper.MusicControl import MusicControl
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Input.Interaction import Interaction
from me.samfreeman.Helper.TextOverlay import TextOverlay
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.GameControl.State import State
from me.samfreeman.Levels.MainMenu import MainMenu
from me.samfreeman.Text.Cutscenes import AllCutscenes
from me.samfreeman.Text.NewUnlock import NewUnlock

frame = simplegui.create_frame("Upside Down", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT, 0)

music = MusicControl()
state = State(music)
menu = MainMenu(frame)
####### EXAMPLE OF HOW TO USE CUTSCENE

acs = AllCutscenes(frame)
cutscenes = acs.allScenes()


player = Player(Vector((50, GV.CANVAS_HEIGHT / 2)), Sprite("images/interactive-sprites/player/PlayerSpriteSheet.png", 30, 20, True), frame, state)

text = TextOverlay("Welcome", "Link")

unlockDisplay = NewUnlock(frame)

inter = Interaction(player, text, cutscenes, state, unlockDisplay)

levelLoader = LevelLoader(player,inter, state)

def update(canvas):
    GV.allow_update = state.levelPlay

    if state.mainMenu:
        menu.draw(canvas)
        music.musicIndex = 0
        music.currentMusic.play()
        inter.checkKeyboard()
    elif state.cutScene:
        cutscenes[0].display(canvas)

        if cutscenes[0].isFinished:
            del cutscenes[0]
            state.cutSceneToLevel()

        inter.checkKeyboard()

    elif state.inLevel:

        if levelLoader.currentLevel.levelComplete() or unlockDisplay.hasUpdated:
            levelLoader.nextlevel()
            unlockDisplay.hasUpdated = False
        levelLoader.currentLevel.draw(canvas)
        text.display(canvas)
        if (levelLoader.currentLevel.player.health <= 0 or levelLoader.currentLevel.player.position.y > GV.CANVAS_HEIGHT):
            state.gameToDeath()
    elif state.weaponPickUp:
        unlockDisplay.display(canvas)
        inter.checkKeyboard()
    elif state.death:
        if (levelLoader.levelCounter < 3):
            speaker = "Link"
        else:
            speaker = "Ghost of Link"

        # text.nextText()
        text.addLine("You died", speaker)
        state.deathToGameOver()

    elif state.gameOver:
        levelLoader.gameOver()


frame.set_draw_handler(update)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.start()
