# Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameControl.LevelLoader import LevelLoader
from me.samfreeman.GameControl.State import State
from me.samfreeman.GameObject.Player import Player
from me.samfreeman.Helper.Cutscene import Cutscene
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Input.Interaction import Interaction
from me.samfreeman.Helper.TextOverlay import TextOverlay
from me.samfreeman.Helper.Sprite import Sprite


frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT, 0)

####### EXAMPLE OF HOW TO USE CUTSCENE
cs = Cutscene(frame)

state = State()

player = Player(Vector((50, GV.CANVAS_HEIGHT - 130)), Sprite("images/interactive-sprites/player/PlayerSpriteSheet.png", 30, 20))

####### EXAMPLE OF HOW TO USE CUTSCENE
cs.setTitle("Part 1: The Beginning")
cs.addText("Samuel", "This is a test to see if the whole system works, I'm really hoping that it does", player.currentSprite.spriteFromIndex([1,1]),
           "Fredsadi", "Yes this test works well, and it is quite cool", player.currentSprite.spriteFromIndex([9,1]))
cs.addText("Samuel", "Thanks for your input,  Bob, it was helpful", player.currentSprite.spriteFromIndex([1,1]),
           "Bob", "Fuck off", player.currentSprite.spriteFromIndex([7,1]))
cs.addText("Lorenzo", "This is the last test to test my function", player.currentSprite.spriteFromIndex([1,1]))

text = TextOverlay("Welcome", "Link")

inter = Interaction(player, text, cs)

music = simplegui._load_local_sound("Music/universe.ogg")

def update(canvas):
    if (levelLoader.currentLevel.player.health <= 0 or levelLoader.currentLevel.player.position.y > GV.CANVAS_HEIGHT):
        if(levelLoader.levelCounter<3):
            speaker = "Link"
        else:
            speaker = "Ghost of Link"
        text.addLine("You died", speaker)
        #text.nextText()
        levelLoader.gameOver()
    if levelLoader.currentLevel.levelComplete():
        levelLoader.nextlevel()
    levelLoader.currentLevel.draw(canvas)
    text.display(canvas)
    music.play()

####### EXAMPLE OF HOW TO USE CUTSCENE

def updateTest(canvas):
    inter.checkKeyboard()
    cs.display(canvas)


levelLoader = LevelLoader(player,inter)
#everytime the game state changes, call this method

frame.set_draw_handler(update)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.start()
