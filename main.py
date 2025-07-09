import shoe
import game
import matplotlib.pyplot as plt

def main():
   Baccarat = game.Game()
   
   results = {'P': 0, 'D': 0, 'T': 0}
   trials = 1000000
   
   for i in range(trials):
      result = Baccarat.play()
      results[result] += 1
      
   withoutTies = results['P'] + results['D']
   trials = withoutTies
   
   print(f"Player wins: {results['P'] / trials * 100:.2f}%")
   print(f"Banker wins: {results['D'] / trials * 100:.2f}%")
   #print(f"Ties: {results['T'] / trials * 100:.2f}%")
   
if __name__ == "__main__":
   main()