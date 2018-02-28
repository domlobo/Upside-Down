try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Keyboard:

    def __init__(self):
        self.left =False
        self.right=False
        self.up=False
        self.down=False

    #handling key press down
    def keyDown(self, key):
        if (key == simplegui.KEY_MAP['right']) or (key == simplegui.KEY_MAP['d']):
            self.right = True
        elif (key == simplegui.KEY_MAP['left']) or (key == simplegui.KEY_MAP['a']):
            self.left = True
        elif (key == simplegui.KEY_MAP['up']) or (key == simplegui.KEY_MAP['space']) or (key == simplegui.KEY_MAP['w']):
            self.up = True
        elif (key == simplegui.KEY_MAP['down']) or (key == simplegui.KEY_MAP['s']):
            self.down = True

    #handling key release
    def keyUp(self, key):
        if (key ==simplegui.KEY_MAP['right']):
            self.right = False
        elif (key == simplegui.KEY_MAP['left']):
            self.left = False
        elif (key == simplegui.KEY_MAP['up']) or (key == simplegui.KEY_MAP['space']):
            self.up = False
        elif (key == simplegui.KEY_MAP['down']):
            self.down = False
