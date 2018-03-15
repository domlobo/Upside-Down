# Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameControl.LevelLoader import LevelLoader
from me.samfreeman.GameObject.Player import Player
from me.samfreeman.Helper.Cutscene import Cutscene
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Input.Interaction import Interaction
from me.samfreeman.Helper.TextOverlay import TextOverlay
from me.samfreeman.Helper.Sprite import Sprite
from me.samfreeman.GameControl.State import State
from me.samfreeman.Levels.MainMenu import MainMenu


frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT, 0)

state = State()
menu = MainMenu()
####### EXAMPLE OF HOW TO USE CUTSCENE

cutscenes = [Cutscene(frame) for i in range(6)]

# cs = Cutscene(frame)


player = Player(Vector((50, GV.CANVAS_HEIGHT - 130)), Sprite("images/interactive-sprites/player/PlayerSpriteSheet.png", 30, 20, True))

####### EXAMPLE OF HOW TO USE CUTSCENE
cutscenes[0].setTitle("Part 1: The Beginning")
cutscenes[0].addText("Samuel", "This is a test to see if the whole system works, I'm really hoping that it does", player.currentSprite.spriteFromIndex([1,1]),
           "Fredsadi", "Yes this test works well, and it is quite cool", player.currentSprite.spriteFromIndex([9,1]))
cutscenes[0].addText("Samuel", "Thanks for your input,  Bob, it was helpful", player.currentSprite.spriteFromIndex([1,1]),
           "Bob", "Fuck off", player.currentSprite.spriteFromIndex([7,1]))
cutscenes[0].addText("Lorenzo", "This is the last test to test my function", player.currentSprite.spriteFromIndex([1,1]))

text = TextOverlay("Welcome", "Link")

inter = Interaction(player, text, cutscenes, state)

music = simplegui._load_local_sound("Music/mii.ogg")

levelLoader = LevelLoader(player,inter, state)

def update(canvas):

    if state.mainMenu:
        menu.draw(canvas)
        inter.checkKeyboard()
    elif state.cutScene:
        cutscenes[0].display(canvas)
        if cutscenes[0].isFinished:
            del cutscenes[0]
            state.cutSceneToLevel()
        inter.checkKeyboard()
    elif state.levelText:
        if levelLoader.currentLevel.levelComplete():
            levelLoader.nextlevel()
        levelLoader.currentLevel.draw(canvas)
        text.display(canvas)
        music.play()
        if (levelLoader.currentLevel.player.health <= 0 or levelLoader.currentLevel.player.position.y > GV.CANVAS_HEIGHT):
            state.gameToDeath()
    elif state.death:
        if (levelLoader.levelCounter < 3):
            speaker = "Link"
        else:
            speaker = "Ghost of Link"

        # text.nextText()
        levelLoader.gameOver()
        text.addLine("You died", speaker)

####### EXAMPLE OF HOW TO USE CUTSCENE

def updateTest(canvas):
    inter.checkKeyboard()
    cs.display(canvas)


#everytime the game state changes, call this method

frame.set_draw_handler(update)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.start()
