import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject
from Player import Player
from Interaction import Interaction
from Enemy import BasicEnemy


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450
state = State()


player = Player(Vector((50, CANVAS_HEIGHT / 2)))
enemy = BasicEnemy(Vector((600, CANVAS_HEIGHT / 2)), 100, player)
inter = Interaction(player)

def draw(canvas):
    update()
    player.draw(canvas, "Green")
    enemy.draw(canvas, "Red")

def update():
    inter.checkKeyboard()

# For developing
frame = simplegui.create_frame("Game Name Goes Here", CANVAS_WIDTH, CANVAS_HEIGHT)

# For Release - Leave last 0
# frame = simplegui.create_frame("Game Name Goes Here", CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.set_mouseclick_handler(inter.clickHandler)
frame.start()