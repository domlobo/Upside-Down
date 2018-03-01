import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject
from Player import Player
from Interaction import Interaction
import GV

GV.CANVAS_WIDTH = 800
GV.CANVAS_HEIGHT = 450
state = State()

player = Player(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2)))
inter = Interaction(player)

def draw(canvas):
    update()
    player.draw(canvas)

def update():
    inter.checkKeyboard()

# For developing
frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT)

# For Release - Leave last 0
# frame = simplegui.create_frame("Game Name Goes Here", CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.set_mouseclick_handler(inter.clickHandler)
frame.start()
