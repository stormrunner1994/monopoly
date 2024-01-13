import Board
import Card
import Player

class Game:
    def __init__(self, numberPlayers):
        self.Board = Board.Board()
        self.NumberPlayers = numberPlayers
        self.Players=[]
        self.Round=0
        
    def StartNewGame(self):
        return
    
    def IsGameFinished(self):
        return
    
    def GetStreetsOfWinner(self):
        return