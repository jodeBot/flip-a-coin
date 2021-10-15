import random

# Class for flipping a coin

class Coin:

    def __init__(self):
        self.__onTop = 'Tales'

    def flip(self):
        if random.randint(0, 1) == 0:
            self.__onTop = 'Tales'
        else:
            self.__onTop = 'Heads'

    def get_onTop(self):
        return self.__onTop
