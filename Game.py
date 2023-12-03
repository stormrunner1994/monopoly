import Board from Board
import Card from Card

class Game:
    def __init__(self, numberPlayers):
        self.Board = Board()
        self.NumberPlayers = numberPlayers
        self.CommunityCards=Card[16]
        self.EventCards=Card[16]
        self.Players=Player[numberPlayer]
        self.Round=0
        
    def StartNewGame(self):
        return
    
    def IsGameFinished(self):
        return
    
    def GetStreetsOfWinner(self):
        return