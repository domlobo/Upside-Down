import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450
state = State()


def draw(canvas):
    update()

def update():
    pass


# For developing
frame = simplegui.create_frame("Game Name Goes Here", CANVAS_WIDTH, CANVAS_HEIGHT)
# For Release - Leave last 0
# frame = simplegui.create_frame("Game Name Goes Here", CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)
frame.start()