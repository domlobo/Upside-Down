# Imports
from me.samfreeman.Helper.Cutscene import Cutscene
from me.samfreeman.Helper.Sprite import Sprite


class AllCutscenes:
    def __init__(self, frame):
        self.all = [Cutscene(frame) for i in range(6)]
        self.playerSprite = Sprite("images/cutscenes/Player_PhoneCall_Right.png", 1, 7, True)
        self.wifeSprite = Sprite("images/cutscenes/Wife_PhoneCall_Left.png", 1, 5, True)
        self.linkSprite = Sprite("images/interactive-sprites/link/link-walk-left.png", 1, 4, True)
        self.unknownSprite = Sprite("images/cutscenes/unknown.png")
        self.bowserSprite = Sprite("images/cutscenes/unkown.png")

        # First

        self.all[0].setTitle("Part 1: The Beginning")
        self.all[0].addText("Bob Froman",
                             "*Grabs tv remove* I     guess today’s going to  be another boring,      useless day *sighs*",
                             self.playerSprite,
                             "Jess Froman", "What’s the matter, Bob?",
                             self.wifeSprite)
        self.all[0].addText("Bob Froman",
                             "Nothing..well, it’s just— no, nevermind",
                             self.playerSprite,
                             "Jess Froman", "Is this how you want to live the rest of your   life Bob? No job, no    money, no purpose",
                             self.wifeSprite)
        self.all[0].addText("Bob Froman",
                             "...Just there’s nothing out there, and I feel   like I can’t do anything – I’m nobody",
                             self.playerSprite,
                             "Jess Froman", "Ok Bob, I’ve set something up for you. Give my  friend a call, he’ll be expecting you.",
                             self.wifeSprite)

        self.all[0].addText("Bob Froman", "Hello, it’s Bob, I was  told to call this number", self.playerSprite,
                            "Link", "Ah, Bob, hello – your   wife told me of how     you’re a failu— how you can’t seem to find a job", self.linkSprite)
        self.all[0].addText("Bob Froman", "Yes to the above, is    there anyway you could  help me?", self.playerSprite,
                            "Link", "There’s one way.. but I don’t know if you’re    ready. Well, there’s    only one way to find out Come to this address.", self.linkSprite)
        self.all[0].addText("Bob Froman", "Ok, do I need to bring  anything?", self.playerSprite,
                            "Link", "A wooden sword.", self.linkSprite)
        self.all[0].addText("Bob Froman", "Well, this will be interesting", self.playerSprite)

        # Second
        self.all[1].setTitle("Part 2: First Contract")
        self.all[1].addText("Bob Froman", "Come on, come on, pick up.", self.playerSprite,
                            "Jess Froman", "*no answer*..*no answer*", self.wifeSprite)
        self.all[1].addText("Bob Froman", "Jess? Honey? Where are  you, I’ve done something", self.playerSprite,
                            "Jess Froman", "Bob, calm down. What is it?", self.wifeSprite)
        self.all[1].addText("Bob Froman", "Your friend.. I’m so    sorry", self.playerSprite,
                            "Jess Froman", "Bob? I can’t hear you? I will see you at home", self.wifeSprite)
        self.all[1].addText("Bob Froman", "Jess? What? Help?", self.playerSprite,
                            "Unknown", "I know", self.unknownSprite)
        self.all[1].addText("Bob Froman", "Hello? Who is this?", self.playerSprite,
                            "Unknown", "I know what you did", self.unknownSprite)
        self.all[1].addText("Bob Froman", "It was an accident", self.playerSprite,
                            "Unknown", "No. It was no accident.  Much power. Such       Strength.", self.unknownSprite)
        self.all[1].addText("Bob Froman", "What do you want from me", self.playerSprite,
                            "Unknown", "I’ll put you through", self.unknownSprite)
        self.all[1].addText("Bob Froman", "Put me through? What? To who?", self.playerSprite,
                            "Bowser", "Hello, I heard what you did to Link. Impressive", self.bowserSprite)
        self.all[1].addText("Bob Froman", "Put me through? What? To who?", self.playerSprite,
                            "Bowser", "Hello, I heard what you did to Link. Impressive", self.bowserSprite)
        self.all[1].addText("Bob Froman", "Who is this? Bowser? Why are you calling me? I  haven't touched Peach", self.playerSprite,
                            "Bowser", "Good. That's not why I'm calling. I need you to do a job for me.", self.bowserSprite)
        self.all[1].addText("Bob Froman", "You have a job? What is it? I need to find a way to provide for my wife.", self.playerSprite,
                            "Bowser", "So many questions. With time, there will be     answers", self.bowserSprite)
        self.all[1].addText("Bob Froman", "I’m listening", self.playerSprite,
                            "Bowser", "Mario. 25 Gold.", self.bowserSprite)
        self.all[1].addText("Bob Froman", "I’m listening", self.playerSprite,
                            "Bowser", "Mario. 25 Gold.", self.bowserSprite)







        # Third
        self.all[2].setTitle("Part 3: Highway To Hell")
        self.all[2].addText("Bob Froman", "Testing", self.playerSprite, "Jess Froman", "Testing 3", self.wifeSprite)

        # Fourth
        self.all[3].setTitle("Part 4: Moving Up In The World")

        # Fifth
        self.all[4].setTitle("Part 5: Disappointment")


    def allScenes(self):
        return self.all