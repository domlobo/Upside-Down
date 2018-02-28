class State:

    def __init__(self):

        # TODO: Work out the game states, and the order in which they will be transitioned a diagram might help.

        self.main_menu = True
        self.stage1 = False
        self.stage2 = False
        self.stage3 = False


    def menuToStage1(self):
        self.main_menu = False
        self.stage1 = True
    # TODO: Have methods for the transitions and such - look at the blackjack game as an example.


