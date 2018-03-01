import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject
from Player import Player
from Interaction import Interaction
from Background import Background
import GV

GV.CANVAS_WIDTH = 800
GV.CANVAS_HEIGHT = 450
state = State()

player = Player(Vector((GV.CANVAS_WIDTH / 2, GV.CANVAS_HEIGHT / 2)))
inter = Interaction(player)
background = Background('https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/Mario-world-empty.jpg?token=APgKaR6TSptYR0qhV63oQBnvXIhsoyFtks5aoRUmwA%3D%3D','','https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario-world-clouds.png?token=APgKafUTHt07IQ0E9ShW18tyX2LJkQL5ks5aoRm7wA%3D%3D')

def draw(canvas):
    update()
    background.update(canvas,player)
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
