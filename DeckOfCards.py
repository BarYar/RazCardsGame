from Card import Card
import random

class DeckOfCards:
    def __init__(self):
        self.deck = []
        suits = ["♣", "♦", "♥", "♠"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10 ,"J" ,"Q", "K", "A"]
        for suit in suits:
            for num in numbers:
                self.deck.append(Card(num, suit))


    def __shuffle(self):
        random.shuffle(self.deck)


    def dealOne(self):
        return self.deck.pop()


    def newGame(self):
        self.__shuffle()


    def show(self):
        print(self.deck)

acard = DeckOfCards()
acard.show()













