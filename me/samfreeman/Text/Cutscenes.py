# Imports
from me.samfreeman.Helper.Cutscene import Cutscene
from me.samfreeman.Helper.Sprite import Sprite


class AllCutscenes:
    def __init__(self, frame):
        self.all = [Cutscene(frame) for i in range(6)]

        # First

        self.all[0].setTitle("Part 1: The Beginning")
        self.all[0].addText("Bob Froman",
                             "This is a test to see if the whole system works, I'm really hoping that it does",
                             Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True),
                             "Froman", "Yes this test works well, and it is quite cool",
                             Sprite("images/cutscenes/Wife_PhoneCall_Left.png", 1, 5, True))
        self.all[0].addText("Bob Froman", "Thanks for your input,  Bob, it was helpful",
                             Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True),
                             "Froman", "Fuck off", Sprite("images/cutscenes/Wife_PhoneCall_Left.png", 1, 5, True))
        self.all[0].addText("Bob Froman", "This is the last test to test my function",
                             Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True))
        # IF YOU WANT THE SPEAKER TO GO FROM SINGLE TO DOUBLE, REPEAT THE TEXT IN THE FIRST SET OF ARGUMENTS
        # AFTER ADDING THE SINGLE
        self.all[0].addText("Bob Froman", "This is the last test to test my function", Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True),
                            "Link", "Yes it works", Sprite("images/interactive-sprites/link/link-walk-left.png", 1, 4, True))


        # Second
        self.all[1].setTitle("Part 1: The Beginning")
        self.all[1].addText("Bob Froman",
                            "This is a test to see if the whole system works, I'm really hoping that it does",
                            Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True),
                            "Froman", "Yes this test works well, and it is quite cool",
                            Sprite("images/cutscenes/Wife_PhoneCall_Left.png", 1, 5, True))
        self.all[1].addText("Bob Froman", "Thanks for your input,  Bob, it was helpful",
                            Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True),
                            "Froman", "Fuck off", Sprite("images/cutscenes/Wife_PhoneCall_Left.png", 1, 5, True))
        self.all[1].addText("Bob Froman", "This is the last test to test my function",
                            Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True))
        # IF YOU WANT THE SPEAKER TO GO FROM SINGLE TO DOUBLE, REPEAT THE TEXT IN THE FIRST SET OF ARGUMENTS
        # AFTER ADDING THE SINGLE
        self.all[1].addText("Bob Froman", "This is the last test to test my function",
                            Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True),
                            "Link", "Yes it works",
                            Sprite("images/interactive-sprites/link/link-walk-left.png", 1, 4, True))

        # Third


        # Fourth


        # Fifth



    def allScenes(self):
        return self.all