import threading
import Game

class Controller:
    def __init__(self):
        self.Results=[]
    
    def StartNewGames(self,numberOfGames):
        numberPlayers=4
        # TODO this in external thread, runs in background
        for index in range(0,numberOfGames-1):
            game = Game.Game(numberPlayers)
            game.StartNewGame()
            self.Results.append(game.GetStreetsOfWinner())
            
    def PrintResults(self):
        for index in range(0,len(self.Results)-1):
            print(self.Results[index])
        
        