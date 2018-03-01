import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject
from Player import Player
from Interaction import Interaction
from LevelLoader import LevelLoader
import GV

state = State()

player = Player(Vector((50, GV.CANVAS_HEIGHT / 2)))

inter = Interaction(player)

# For Release - remove last bracket and uncomment
frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT)#, 0)

levelLoader = LevelLoader(player,inter)
#everytime the game state changes, call this method
frame = levelLoader.nextlevel(frame)

frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.set_mouseclick_handler(inter.clickHandler)
frame.start()
