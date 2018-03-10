# Imports
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import me.samfreeman.GameControl.GV as GV
from me.samfreeman.GameControl.LevelLoader import LevelLoader
from me.samfreeman.GameControl.State import State
from me.samfreeman.GameObject.Player import Player
from me.samfreeman.Helper.Vector import Vector
from me.samfreeman.Input.Interaction import Interaction
from me.samfreeman.Helper.TextOverlay import TextOverlay
from me.samfreeman.Helper.Sprite import Sprite

state = State()

player = Player(Vector((50, GV.CANVAS_HEIGHT - 130)), Sprite("images/interactive-sprites/player/PlayerSpriteSheet.png", True, 30, 20))


text = TextOverlay("Welcome", "Link")

inter = Interaction(player, text)


def update(canvas):
    if (levelLoader.currentLevel.player.health <= 0 or levelLoader.currentLevel.player.position.y > GV.CANVAS_HEIGHT):
        if(levelLoader.levelCounter<3):
            speaker = "Link"
        else:
            speaker = "Ghost of Link"
        text.addLine("You died", speaker)
        #text.nextText()
        levelLoader.gameOver()
    if levelLoader.currentLevel.levelComplete():
        levelLoader.nextlevel()
    levelLoader.currentLevel.draw(canvas)
    text.display(canvas)

# For Release - remove last bracket and uncomment
frame = simplegui.create_frame("Game Name Goes Here", GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT, 0)

levelLoader = LevelLoader(player,inter)
#everytime the game state changes, call this method

frame.set_draw_handler(update)
frame.set_keydown_handler(inter.keyboard.keyDown)
frame.set_keyup_handler(inter.keyboard.keyUp)
frame.start()
