try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import me.samfreeman.GameControl.GV as GV

from me.samfreeman.Helper.Vector import Vector


class Background:

    #called from level.__init__
    def __init__(self, farBackground, foreground="", clouds=""):
        #furthest back background
        self.FAR_BACKGROUND_LOAD = simplegui._load_local_image(farBackground)
        self.FAR_BACKGROUND_HEIGHT = self.FAR_BACKGROUND_LOAD.get_height()
        self.FAR_BACKGROUND_WIDTH = self.FAR_BACKGROUND_LOAD.get_width()
        self.FAR_BACKGROUND_CENTER = Vector((self.FAR_BACKGROUND_WIDTH/2, self.FAR_BACKGROUND_HEIGHT/2))
        self.farBackgroundPos = Vector((self.FAR_BACKGROUND_WIDTH / 2, GV.CANVAS_HEIGHT / 2))
        self.farBackgroundVel = Vector((0,0))

        #map foreground
        self.FOREGROUND_LOAD = simplegui._load_local_image(foreground)
        self.FOREGROUND_HEIGHT = self.FOREGROUND_LOAD.get_height()
        self.FOREGROUND_WIDTH = self.FOREGROUND_LOAD.get_width()
        self.FOREGROUND_CENTER = Vector((self.FOREGROUND_WIDTH/2, self.FOREGROUND_HEIGHT/2))
        self.foregroundPos = Vector((self.FOREGROUND_WIDTH / 2, GV.CANVAS_HEIGHT / 2))
        self.foregroundVel = Vector((0,0))

        #clouds
        self.CLOUD_LOAD = simplegui._load_local_image(clouds)
        self.CLOUD_HEIGHT = self.CLOUD_LOAD.get_height()
        self.CLOUD_WIDTH = self.CLOUD_LOAD.get_width()
        self.CLOUD_CENTER = Vector((self.CLOUD_WIDTH/2, self.CLOUD_HEIGHT/2))
        self.cloudOnePos = Vector((self.CLOUD_WIDTH / 2, GV.CANVAS_HEIGHT / 2))
        self.cloudTwoPos = Vector((self.CLOUD_WIDTH * 1.5, GV.CANVAS_HEIGHT / 2))
        self.cloudVel = Vector((-3,0))

    #called from level.levelComplete
    def isStillRunning(self):
        return self.foregroundPos.x >(-self.foregroundPos.x/2)

    #update the position of the background if the player is in the right position
    #called from the draw method of level
    def update(self,canvas, player):
        if(self.cloudOnePos.x<-(self.CLOUD_WIDTH /2)):
            self.cloudOnePos.x = self.CLOUD_WIDTH*1.5
        if(self.cloudTwoPos.x<-(self.CLOUD_WIDTH/2)):
            self.cloudTwoPos.x = self.CLOUD_WIDTH*1.5

        if (player.position.x > GV.CANVAS_WIDTH/2)and(self.isStillRunning()) and (player.velocity.x > 1):
            #variable acceleration depending on position of the player
            movementFactor = (player.position.x - GV.CANVAS_WIDTH / 2) / (GV.CANVAS_WIDTH / 2)
            #move foreground and backgroud different amounts
            self.farBackgroundVel= Vector((-3 * movementFactor,0))
            self.foregroundVel= Vector((-10*movementFactor,0))

        self.cloudOnePos.add(self.cloudVel)
        self.cloudTwoPos.add(self.cloudVel)
        self.farBackgroundPos.add(self.farBackgroundVel)
        self.foregroundPos.add(self.foregroundVel)
        #draw total background in
        canvas.draw_image(self.FAR_BACKGROUND_LOAD,self.FAR_BACKGROUND_CENTER.getP(),(self.FAR_BACKGROUND_WIDTH,self.FAR_BACKGROUND_HEIGHT),self.farBackgroundPos.getP(),(self.FAR_BACKGROUND_WIDTH,self.FAR_BACKGROUND_HEIGHT))
        canvas.draw_image(self.FOREGROUND_LOAD,self.FOREGROUND_CENTER.getP(),(self.FOREGROUND_WIDTH,self.FOREGROUND_HEIGHT),self.foregroundPos.getP(),(self.FOREGROUND_WIDTH, self.FOREGROUND_HEIGHT))
        canvas.draw_image(self.CLOUD_LOAD,self.CLOUD_CENTER.getP(),(self.CLOUD_WIDTH,self.CLOUD_HEIGHT),self.cloudOnePos.getP(),(self.CLOUD_WIDTH,self.CLOUD_HEIGHT))
        canvas.draw_image(self.CLOUD_LOAD,self.CLOUD_CENTER.getP(),(self.CLOUD_WIDTH,self.CLOUD_HEIGHT),self.cloudTwoPos.getP(),(self.CLOUD_WIDTH,self.CLOUD_HEIGHT))
