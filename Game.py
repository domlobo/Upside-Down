import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject
from Player import Player
from Interaction import Interaction
from Level import Level
import GV


state = State()

player = Player(Vector((50, GV.CANVAS_HEIGHT / 2)))

inter = Interaction(player)
levelOne = Level('https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-1.1.jpg?token=APgKaY-Q3e5QVhZ-H89jyYEck_xcLGKSks5aoWDHwA%3D%3D','','https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-clouds.png?token=APgKaSIkI0DepOY41ozT1p6k03q-8_-vks5aoT75wA%3D%3D', player)


def draw(canvas):
    update()
    levelOne.background.update(canvas,player)
    player.draw(canvas, "Green")
    for proj in player.projectiles:
        proj.draw(canvas, "Blue")
    for enemy in levelOne.enemies:
        enemy.draw(canvas, "Red")

def update():
    levelOne.collInter.update()
    inter.checkKeyboard()

# For developing
#frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT)

# For Release - Leave last 0
frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.set_mouseclick_handler(inter.clickHandler)
frame.start()
