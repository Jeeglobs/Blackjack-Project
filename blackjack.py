class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.cards = []

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def add_cards(self):
        


class Player:
    pass


class Dealer:
    pass


class Game:

    def __init__(self, player, dealer, deck):
        self.player = None
        self.dealer = None
        self.deck = None

    def setup(self):
        deck1 = Deck()
        deck1.add_cards()
        for card in deck1.cards:
            print(card)


new_game = Game()
new_game.setup()
