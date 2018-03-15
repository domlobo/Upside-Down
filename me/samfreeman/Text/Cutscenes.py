# Imports
from me.samfreeman.Helper.Sprite import Sprite


class AllCutscenes:
    def __init__(self):
        self.all = []

        # First

        self.all[0].setTitle("Part 1: The Beginning")
        self.all[0].addText("Samuel",
                             "This is a test to see if the whole system works, I'm really hoping that it does",
                             player.currentSprite.spriteFromIndex([1, 1]),
                             "Fredsadi", "Yes this test works well, and it is quite cool",
                             player.currentSprite.spriteFromIndex([9, 1]))
        self.all[0].addText("Samuel", "Thanks for your input,  Bob, it was helpful",
                             player.currentSprite.spriteFromIndex([1, 1]),
                             "Bob", "Fuck off", player.currentSprite.spriteFromIndex([7, 1]))
        self.all[0].addText("Lorenzo", "This is the last test to test my function",
                             player.currentSprite.spriteFromIndex([1, 1]))


        # Second


        # Third


        # Fourth


        # Fifth



    def allScenes(self):
        return self.all