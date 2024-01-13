import Street
import CardTypes
import Card

class Board:
    def __init__(self):
        self.Streets=[40]
        self.CommunityCards=[16]
        self.EventCards=[16]
        
        
    def _GetCommunityCards(self):       
        self.CommunityCards = []
        self.CommunityCards.append(Card.Card({CardTypes.MoveToNextBall:-1, CardTypes.OwnerGetsDoubleRent:-1}))
        self.CommunityCards.append(Card.Card({CardTypes.PayMoneyToCenter:15}))
        self.CommunityCards.append(Card.Card({CardTypes.GoBackThreeFields:-1}))        
        self.CommunityCards.append(Card.Card({CardTypes.LeaveFromPrison:-1}))        
        self.CommunityCards.append(Card.Card({CardTypes.MoveToFieldIndex:23})) 
        self.CommunityCards.append(Card.Card({CardTypes.MoveToFieldIndex:0}))
        self.CommunityCards.append(Card.Card({CardTypes.MoveToFieldIndex:39}))
        self.CommunityCards.append(Card.Card({CardTypes.MoveToFieldIndex:4}))
        self.CommunityCards.append(Card.Card({CardTypes.RenovationOfSupermarkets:25,CardTypes.RenovationOfPokecenters:100}))        
        self.CommunityCards.append(Card.Card({CardTypes.GetMoneyFromBank:50}))
        self.CommunityCards.append(Card.Card({CardTypes.GoToPrison:-1}))        
        self.CommunityCards.append(Card.Card({CardTypes.GoToPrison:-1}))