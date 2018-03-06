# Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameControl.LevelLoader import LevelLoader
from me.samfreeman.GameControl.State import State
from me.samfreeman.GameObject.Player import Player
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Input.Interaction import Interaction
from me.samfreeman.Helper.Sprite import Sprite

state = State()

player = Player(Vector((50, GV.CANVAS_HEIGHT - 80)), Sprite("images/interactive-sprites/player/walk_left_test.png"))

inter = Interaction(player)

def update(canvas):
    if levelLoader.currentLevel.levelComplete():
        levelLoader.nextlevel()
    levelLoader.currentLevel.draw(canvas)

# For Release - remove last bracket and uncomment
frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT)#, 0)

levelLoader = LevelLoader(player,inter)
#everytime the game state changes, call this method

frame.set_draw_handler(update)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.set_mouseclick_handler(inter.clickHandler)
frame.start()
