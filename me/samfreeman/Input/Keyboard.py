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
        self.tryWeapon=0

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
        if (key == simplegui.KEY_MAP['q']):
            self.enter = True
        #handling weapon changes
        if (key == simplegui.KEY_MAP['1']):
            self.tryWeapon = 1
        if (key == simplegui.KEY_MAP['2']):
            self.tryWeapon = 2
        if (key == simplegui.KEY_MAP['3']):
            self.tryWeapon = 3

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
        elif (key == simplegui.KEY_MAP['q']):
            self.enter=False
