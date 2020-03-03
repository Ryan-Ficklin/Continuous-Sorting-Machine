from Deck import Deck
class ContinuousSortingMachine(object):
        def __init__(self):
            self.create()
        def create(self):
            self.CSM = []
            deckNum = int(input("How many decks would you like to put into the machine? "))
            for i in range(deckNum):
                 self.CSM.append(Deck)
        def print(self):
            print(self.CSM)
                
