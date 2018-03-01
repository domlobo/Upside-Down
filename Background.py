try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import GV

class Background:

    def __init__(self, farBackground, foreground, clouds):
        #furthest back background
        self.FAR_BACKGROUND_LOAD = simplegui.load_image(farBackground)
        self.FAR_BACKGROUND_HEIGHT = FAR_BACKGROUND_LOAD.get_height()
        self.FAR_BACKGROUND_WIDTH = FAR_BACKGROUND_LOAD.get_width()
        self.farBackgroundPos = [self.FAR_BACKGROUND_WIDTH, self.FAR_BACKGROUND_HEIGHT]

        #map foreground
        self.FOREGROUND_LOAD = simplegui.load_image(foreground)
        self.FOREGROUND_HEIGHT = FOREGROUND_LOAD.get_height()
        self.FOREGROUND_WIDTH = FOREGROUND_LOAD.get_width()
        self.foregroundPos = [self.FOREGROUND_WIDTH, self.FOREGROUND_HEIGHT]

        #clouds
        self.clouds = simplegui.load_image(clouds)
        self.CLOUD_HEIGHT = CLOUD_LOAD.get_height()
        self.CLOUD_WIDTH = CLOUD_LOAD.get_width()
        self.cloudPos = [self.CLOUD_WIDTH, self.CLOUD_HEIGHT]

    def update(self, player):
