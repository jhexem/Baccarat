import numpy as np

class Shoe:
   cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
   values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 0,
               'J': 0, 'Q': 0, 'K': 0, 'A': 1}
   
   def __init__(self, numDecks=6):
      self.numDecks = numDecks
      self.deck = self.createDeck()
      self.shuffle()
      
   def createDeck(self):
      deck = []
      for _ in range(self.numDecks * 4):
         for card in self.cards:
            deck.append(card)
      return deck
      
   def dealCard(self):
      if len(self.deck) == 0:
         raise ValueError("No cards left in the shoe.")
      return self.deck.pop()
   
   def shuffle(self):
      self.deck = self.createDeck()
      np.random.shuffle(self.deck)
      
   def getValue(self, card):
      return self.values[card]
   
   def remainingCards(self):
      return len(self.deck)