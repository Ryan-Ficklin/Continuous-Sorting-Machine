from Card import Card
class Deck(object):
    
    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(card) for card in self.cards) + ']'
    
    def create(self):
        self.cards = []
        for i in range(4):
            for j in range(0,14):
                self.cards.append(Card(i, j))
                
