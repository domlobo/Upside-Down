import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject
from Player import Player
from Interaction import Interaction
from Background import Background
import GV
from Enemy import BasicEnemy

state = State()

player = Player(Vector((50, GV.CANVAS_HEIGHT / 2)))
enemy = BasicEnemy(Vector((600, GV.CANVAS_HEIGHT / 2)), 100, player)
inter = Interaction(player)
background = Background('https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/player/images/background/Mario-world-1.1.jpg?token=APgKacyvB6C2WUUWnobOTvt_toujcGJRks5aoTb-wA%3D%3D','','https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/Mario-world-clouds.png?token=APgKaf06O01OJerNk_hhSheR-13nhXbqks5aoTd4wA%3D%3D')

def draw(canvas):
    update()
    background.update(canvas,player)
    player.draw(canvas, "Green")

    enemy.draw(canvas, "Red")

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
