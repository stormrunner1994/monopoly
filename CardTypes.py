from enum import Enum

class CardTypes(Enum):
    PayMoneyToBank=1
    PayMoneyToCenter=2
    GetMoneyFromBank=3
    MoveToNextBall=4    
    OwnerGetsDoubleRent=5
    GoBackThreeFields=6
    LeaveFromPrison=7
    MoveToFieldIndex=8
    RenovationOfSupermarkets=9
    RenovationOfPokecenters=10    
    GoToPrison=11
    GoToZapdosOrArctos=11