import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from State import State
from Vector import Vector
from GameObject import GameObject
from Player import Player
from Interaction import Interaction
from LevelLoader import LevelLoader
import GV

state = State()

player = Player(Vector((50, GV.CANVAS_HEIGHT - 80)))

inter = Interaction(player)

#commenting to fix merge conflict
# enemies = [BasicEnemy(Vector((600, GV.CANVAS_HEIGHT - 131)), 100, player), BasicEnemy(Vector((800, GV.CANVAS_HEIGHT - 131)), 100, player)]

# inter = Interaction(player)
# collInter = PlayerEnemyInteraction(player, enemies)
# background = Background('https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-1.1.jpg?token=APgKaY-Q3e5QVhZ-H89jyYEck_xcLGKSks5aoWDHwA%3D%3D','','https://raw.githubusercontent.com/domlobo/CS1830-Games-Lab/master/images/background/mario/Mario-world-clouds.png?token=APgKaSIkI0DepOY41ozT1p6k03q-8_-vks5aoT75wA%3D%3D')

# def draw(canvas):
#     update()
#     background.update(canvas,player)
#     player.draw(canvas, "Green")
#     for proj in player.projectiles:
#         proj.draw(canvas, "Blue")
#     for enemy in enemies:
#         enemy.draw(canvas, "Red")
# >>>>>>> master

def update(canvas):
    if levelLoader.currentLevel.levelComplete():
        levelLoader.nextlevel
    levelLoader.currentLevel.draw(canvas)

# For Release - remove last bracket and uncomment
frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT)#, 0)

levelLoader = LevelLoader(player,inter)
#everytime the game state changes, call this method

frame.set_draw_handler(update)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.set_mouseclick_handler(inter.clickHandler)
frame.start()
