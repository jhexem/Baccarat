import shoe
class Game:
   def __init__(self, numDecks=6, show=False):
      self.shoe = shoe.Shoe(numDecks)
      self.playerHand = []
      self.dealerHand = []
      self.playerScore = 0
      self.dealerScore = 0
      self.show = show
      self.needShuffle = False
      
   def dealHands(self):
      self.playerHand = [self.shoe.dealCard(), self.shoe.dealCard()]
      self.dealerHand = [self.shoe.dealCard(), self.shoe.dealCard()]
   
   def calculateScores(self):
      self.playerScore = sum(self.shoe.getValue(card) for card in self.playerHand) % 10
      self.dealerScore = sum(self.shoe.getValue(card) for card in self.dealerHand) % 10
      
   def checkNatural(self):
      if self.playerScore in ['8', '9'] or self.dealerScore in ['8', '9']:
         return True
      return False
   
   def determineWinner(self):
      if self.playerScore > self.dealerScore:
         return 'P'
      elif self.playerScore < self.dealerScore:
         return 'D'
      else:
         return 'T'
      
   def displayHands(self):
      print(f"Player's Hand: {self.playerHand} (Score: {self.playerScore})")
      print(f"Dealer's Hand: {self.dealerHand} (Score: {self.dealerScore})")
      
   def displayResult(self, result):
      if result == 'P':
         print("Player wins!")
      elif result == 'D':
         print("Dealer wins!")
      else:
         print("It's a tie!")
      
   def play(self):
      if self.needShuffle:
         self.shoe.shuffle()
         self.needShuffle = False
      self.dealHands()
      self.calculateScores()
      if self.shoe.remainingCards() <= 7:
         self.needShuffle = True
      if self.show:
         self.displayHands()
      if self.checkNatural():
         winner = self.determineWinner()
         if self.show:
            self.displayResult(winner)
         return winner
      if self.playerScore <= 5:
         self.playerHand.append(self.shoe.dealCard())
      if len(self.playerHand) == 2:
         if self.dealerScore <= 5:
            self.dealerHand.append(self.shoe.dealCard())
      elif len(self.playerHand) == 3:
         if self.dealerScore <= 2:
            self.dealerHand.append(self.shoe.dealCard())
         elif self.dealerScore == 3 and self.playerHand[2] != '8':
            self.dealerHand.append(self.shoe.dealCard())
         elif self.dealerScore == 4 and self.playerHand[2] in ['2', '3', '4', '5', '6', '7']:
            self.dealerHand.append(self.shoe.dealCard())
         elif self.dealerScore == 5 and self.playerHand[2] in ['4', '5', '6', '7']:
            self.dealerHand.append(self.shoe.dealCard())
         elif self.dealerScore == 6 and self.playerHand[2] in ['6', '7']:
            self.dealerHand.append(self.shoe.dealCard())
      else:
         return "Error: Invalid hand length."
      self.calculateScores()
      winner = self.determineWinner()
      if self.show:
         self.displayHands()
         self.displayResult(winner)
      return winner