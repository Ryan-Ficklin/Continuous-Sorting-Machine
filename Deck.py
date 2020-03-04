from Card import Card
import random
class Deck(object):
    
    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(card) for card in self.cards) + ']'
    
    def create(self):
        self.cards = []
        for i in range(4):
            for j in range(0,13):
                self.cards.append(Card(i, j))

    def shuffle(self):
        n = len(self.cards)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            self.cards[i],self.cards[j] = self.cards[j],self.cards[i]
                
