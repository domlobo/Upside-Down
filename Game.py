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
class Game:

    def __init__(self):
        self.music = MusicControl()
        self.state = State(self.music)
        self.menu = MainMenu(frame)
        self.reset()
        # self.acs = AllCutscenes(frame)
        # self.cutscenes = self.acs.allScenes()
        # self.player = Player(Vector((50, GV.CANVAS_HEIGHT / 2)),
        #                      Sprite("images/interactive-sprites/player/PlayerSpriteSheet.png", 30, 20, True), frame,
        #                      self.state)
        # self.text = TextOverlay("Welcome", 0)
        # self.unlockDisplay = NewUnlock(frame)
        # self.inter = Interaction(self.player, self.text, self.cutscenes, self.state, self.unlockDisplay)
        # self.levelLoader = LevelLoader(self.player, self.inter, self.state)
    def reset(self):

        self.state = State(self.music)
        self.acs = AllCutscenes(frame)

        self.cutscenes = self.acs.allScenes()
        self.player = Player(Vector((50, GV.CANVAS_HEIGHT / 2)),
                             Sprite("images/interactive-sprites/player/PlayerSpriteSheet.png", 30, 20, True), frame,
                             self.state)
        self.text = TextOverlay("Welcome", 0)
        self.unlockDisplay = NewUnlock(frame)
        self.inter = Interaction(self.player, self.text, self.cutscenes, self.state, self.unlockDisplay)
        self.levelLoader = LevelLoader(self.player, self.inter, self.state)
        GV.win = False
        GV.on_last = False

    def loop(self, canvas):
        # make it loop
        self.music.currentMusic.play()

        if self.state.mainMenu:
            # print("loop - mm")
            self.menu.draw(canvas)
            self.music.musicIndex = 0
            self.inter.checkKeyboard()
        elif self.state.cutScene:
            # print("loop - cs")

            self.cutscenes[0].display(canvas)

            if self.cutscenes[0].isFinished:
                del self.cutscenes[0]
                self.state.cutSceneToLevel()

            self.inter.checkKeyboard()

        elif self.state.inLevel:
            GV.allow_update = self.state.levelPlay
            if self.levelLoader.currentLevel.levelComplete() or self.unlockDisplay.hasUpdated:
                self.levelLoader.nextlevel()
                self.unlockDisplay.hasUpdated = False
            self.levelLoader.currentLevel.draw(canvas)
            self.text.display(canvas)
            if (self.levelLoader.currentLevel.player.health <= 0 or self.levelLoader.currentLevel.player.position.y > GV.CANVAS_HEIGHT):
                self.state.gameToDeath()
        elif self.state.weaponPickUp:
            self.unlockDisplay.display(canvas)
            self.inter.checkKeyboard()
        elif self.state.death:
            if (self.levelLoader.levelCounter < 3):
                speaker = 0
            else:
                speaker = 5

            # text.nextText()
            self.text.addLine("You died", speaker)
            self.state.deathToGameOver()

        elif self.state.gameOver:
            self.levelLoader.gameOver()

        elif self.state.score:
            self.inter.checkKeyboard()

        if GV.need_reset:
            canvas.draw_text("LOADING...", ((GV.CANVAS_WIDTH - frame.get_canvas_textwidth("LOADING...", 30)) / 2, GV.CANVAS_HEIGHT / 6), 30, "White")
            self.reset()
            GV.need_reset = False

game = Game()
frame.set_draw_handler(game.loop)
frame.set_keydown_handler(game.inter.keyboard.keyDown)
frame.set_keyup_handler(game.inter.keyboard.keyUp)
frame.start()
