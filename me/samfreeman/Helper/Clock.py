class Clock:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1

    def transition(self, frameDuration):
        return self.time % frameDuration == 0

    # def transition(self, rate):
    #     return self.time % (60 / rate) == 0