# Imports
from me.samfreeman.Helper.Cutscene import Cutscene
from me.samfreeman.Helper.Sprite import Sprite


class AllCutscenes:
    def __init__(self, frame):
        self.all = [Cutscene(frame) for i in range(6)]
        self.playerSprite = Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True)
        self.wifeSprite = Sprite("images/cutscenes/Wife_PhoneCall_Left.png", 1, 5, True)
        self.linkSprite = Sprite("images/interactive-sprites/link/link-walk-left.png", 1, 4, True)
        # First

        self.all[0].setTitle("Part 1: The Beginning")
        self.all[0].addText("Bob Froman",
                             "This is a test to see if the whole system works, I'm really hoping that it does",
                             self.playerSprite,
                             "Jess Froman", "Yes this test works well, and it is quite cool",
                             self.wifeSprite)
        self.all[0].addText("Bob Froman", "Thanks for your input,  Bob, it was helpful",
                             self.playerSprite,
                             "Jess Froman", "Fuck off", self.wifeSprite)
        self.all[0].addText("Bob Froman", "This is the last test to test my function",
                             self.playerSprite)
        # IF YOU WANT THE SPEAKER TO GO FROM SINGLE TO DOUBLE, REPEAT THE TEXT IN THE FIRST SET OF ARGUMENTS
        # AFTER ADDING THE SINGLE
        self.all[0].addText("Bob Froman", "This is the last test to test my function", self.playerSprite,
                            "Link", "Yes it works", self.linkSprite)


        # Second
        self.all[1].setTitle("Part 2: First Contract")
        self.all[1].addText("Bob Froman", "Testing", self.playerSprite, "Jess Froman", "Testing 3", self.wifeSprite)
        self.all[1].addText("Bob Froman", "Testing", self.playerSprite, "Jess Froman", "Testing 3", self.wifeSprite)
        # Third
        self.all[2].setTitle("Part 3: Highway To Hell")
        self.all[2].addText("Bob Froman", "Testing", self.playerSprite, "Jess Froman", "Testing 3", self.wifeSprite)

        # Fourth
        self.all[3].setTitle("Part 4: Moving Up In The World")

        # Fifth
        self.all[4].setTitle("Part 5: Disappointment")


    def allScenes(self):
        return self.all