import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject
from Player import Player
from Interaction import Interaction
from Background import Background
import GV
from Enemy import BasicEnemy
from PlayerEnemyInteraction import PlayerEnemyInteraction

state = State()

player = Player(Vector((50, GV.CANVAS_HEIGHT - 31)))

enemies = [BasicEnemy(Vector((600, GV.CANVAS_HEIGHT - 31)), 100, player), BasicEnemy(Vector((800, GV.CANVAS_HEIGHT - 31)), 100, player)]

inter = Interaction(player)
collInter = PlayerEnemyInteraction(player, enemies)
background = Background('https://raw.githubusercontent.com/domlobo/CS18GV.CANVAS_HEIGHT - 30-Games-Lab/player/images/background/Mario-world-1.1.jpg?token=APgKacyvB6C2WUUWnobOTvt_toujcGJRks5aoTb-wA%3D%3D','','https://raw.githubusercontent.com/domlobo/CS18GV.CANVAS_HEIGHT - 30-Games-Lab/master/images/background/mario/Mario-world-clouds.png?token=APgKaSIkI0DepOY41ozT1p6k03q-8_-vks5aoT75wA%3D%3D')

def draw(canvas):
    update()
    background.update(canvas,player)
    player.draw(canvas, "Green")
    for proj in player.projectiles:
        proj.draw(canvas, "Blue")
    for enemy in enemies:
        enemy.draw(canvas, "Red")

def update():
    collInter.update()
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
