from Deck import Deck
import random
class ContinuousSortingMachine(object):
        def __init__(self):
                self.create()
        def __str__(self):
                return '[' + ', '.join(str(card) for card in self.CSM) + ']'
        def create(self):
                self.CSM = []
                self.deckNum = int(input("How many decks would you like to put into the machine? "))
                for i in range(self.deckNum):
                        for j in range(52):
                                self.CSM.append(Deck().cards[j])
        def shuffle(self):
                n = len(self.CSM)
                for i in range(n-1,0,-1): 
                        j = random.randint(0,i+1) 
                        self.CSM[i],self.CSM[j] = self.CSM[j],self.CSM[i]
        def deal(self):
                self.deals = []
                numDealt = int(input("How many cards would you like to be dealt? "))
                for i in range(numDealt):
                        print(f"{self.CSM[i]}")
                        self.deals.append(self.CSM[i])
                        self.CSM.pop(i)
        def recycle(self):
                for i in range(len(self.deals)):
                        self.CSM.append(self.deals[i])


                        
                
                
                               
                
