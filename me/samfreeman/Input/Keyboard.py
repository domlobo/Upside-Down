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
        self.enter=False
        self.j = False
        self.k = False

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

        if (key == simplegui.KEY_MAP['j']):
            self.j = True
        if (key == simplegui.KEY_MAP['k']):
            self.k = True
        if (key == simplegui.KEY_MAP['q']):
            self.enter = True


    #handling key release
    def keyUp(self, key):
        if (key == simplegui.KEY_MAP['right']) or (key == simplegui.KEY_MAP['d']):
            self.right = False
        elif (key == simplegui.KEY_MAP['left'])or (key == simplegui.KEY_MAP['a']):
            self.left = False
        elif (key == simplegui.KEY_MAP['up']) or (key == simplegui.KEY_MAP['space'] or (key == simplegui.KEY_MAP['w'])):
            self.up = False
        elif (key == simplegui.KEY_MAP['down'])or (key == simplegui.KEY_MAP['s']):
            self.down = False

        if (key == simplegui.KEY_MAP['j']):
            self.j = False
        if (key == simplegui.KEY_MAP['k']):
            self.k = False
        elif (key == simplegui.KEY_MAP['q']):
            self.enter=False
