try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import GV
from Vector import Vector

class Background:

    def __init__(self, farBackground, foreground="", clouds=""):
        #furthest back background
        self.FAR_BACKGROUND_LOAD = simplegui.load_image(farBackground)
        self.FAR_BACKGROUND_HEIGHT = FAR_BACKGROUND_LOAD.get_height()
        self.FAR_BACKGROUND_WIDTH = FAR_BACKGROUND_LOAD.get_width()
        self.FAR_BACKGROUND_CENTER = Vector(self.FAR_BACKGROUND_WIDTH/2, self.FAR_BACKGROUND_HEIGHT/2)
        self.farBackgroundPos = Vector(self.FAR_BACKGROUND_WIDTH/2, GV.CANVAS_HEIGHT/2)

        #map foreground
        self.FOREGROUND_LOAD = simplegui.load_image(foreground)
        self.FOREGROUND_HEIGHT = FOREGROUND_LOAD.get_height()
        self.FOREGROUND_WIDTH = FOREGROUND_LOAD.get_width()
        self.FOREGROUND_CENTER = Vector(self.FOREGROUND_WIDTH/2, self.FOREGROUND_HEIGHT/2)
        self.foregroundPos = Vector(self.FOREGROUND_WIDTH/2, GV.CANVAS_HEIGHT/2)

        #clouds
        self.clouds = simplegui.load_image(clouds)
        self.CLOUD_HEIGHT = CLOUD_LOAD.get_height()
        self.CLOUD_WIDTH = CLOUD_LOAD.get_width()
        self.CLOUD_CENTER = Vector(self.CLOUD_WIDTH/2, self.CLOUD_HEIGHT/2)
        self.cloudPos = Vector(self.CLOUD_WIDTH/2,GV.CANVAS_HEIGHT/2)

    #update the position of the background if the player is in the right position
    def update(self, player):
        self.cloudPos.x -= 3
        if (player.position.x > GV.CANVAS_WIDTH/2) and (player.position.y > GV.CANVAS_HEIGHT/2):
            #variable acceleration depending on position of the player
            movementFactor = (player.position.x - GV.CANVAS_WIDTH/2)/400
            #move foreground and backgroud different amounts
            self.farBackgroundPos.x -= 10 * movementFactor
            self.foregroundPos.x -= 30*movementFactor
        #draw background and foreground in
        simplegui.draw_image(self.FAR_BACKGROUND_LOAD,self.FAR_BACKGROUND_CENTER.getP(),(self.FAR_BACKGROUND_WIDTH,self.FAR_BACKGROUND_HEIGHT),self.farBackgroundPos.getP(),(GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT))
        simplegui.draw_image(self.FOREGROUND_LOAD,self.FOREGROUND_CENTER.getP(),(self.FOREGROUND_WIDTH,self.FOREGROUND_HEIGHT),self.foregroundPos.getP(),(GV.CANVAS_WIDTH, GV.CANVAS_HEIGHT))
