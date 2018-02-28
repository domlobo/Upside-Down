import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450
state = State()

# Testing game object
gameob = GameObject(Vector((100, 100)), Vector((2, 0)), [20, 50], 100)

def draw(canvas):
    update()
    gameob.draw(canvas)

def update():
    gameob.update()

frame = simplegui.create_frame("Game Name Goes Here", CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)
frame.start()