import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450
state = State()

# Testing game object
#gameob = GameObject(Vector((100, 100)), Vector((2, 0)), [20, 50], 100)
player = Player(Vector(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2))
inter = Interaction(player)

def draw(canvas):
    update()
    player.draw()

def update():
    pass

# For developing
frame = simplegui.create_frame("Game Name Goes Here", CANVAS_WIDTH, CANVAS_HEIGHT)
# For Release - Leave last 0
# frame = simplegui.create_frame("Game Name Goes Here", CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)
frame.set_keydown_handler(inter.keyboard.keyDown())
frame.set_keyup_handler(inter.keyboard.keyUp())
frame.set_mouseclick_handler(inter.clickHanler())
frame.start()