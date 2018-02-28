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

    def keyDown(self, key):
        if key ==simplegui.KEY_MAP['right']:
            self.right = True
        elif key == simplegui.KEY_MAP['left']:
            self.left = True
        elif key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['space']:
            self.up = True
        elif key == simplegui.KEY_MAP['down']:
            self.down = True

    def keyUp(self, key):
        if key ==simplegui.KEY_MAP['right']:
            self.right = False
        elif key == simplegui.KEY_MAP['left']:
            self.left = False
        elif key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['space']:
            self.up = False
        elif key == simplegui.KEY_MAP['down']:
            self.down = False
