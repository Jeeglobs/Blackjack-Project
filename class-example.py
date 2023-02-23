import random

SUITS = ['♥️', '♣️', '♠️', '♦️']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit=None, rank=None):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'

    # def get_rank(self):
    #     return self.rank


class Deck:
    def __init__(self):
        self.cards = []
        self.add_cards()

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.hand = []

    def __str__(self):
        return f'{self.name} is the player'

    def view_cards(self):
        for card in self.hand:
            print(card)

    def turn(self):
        # player decides how many times to hit before staying
        pass


class Dealer():
    # inherits methods from Player
    # everything is the same as Player unless overridden
    def __init__(self):
        self.name = 'Dealer'
        # overrides the input for name in Player
        self.hand = []

    def __str__(self):
        return f'{self.name} is the dealer'

    def view_cards(self):
        for card in self.hand:
            print(card)

    def turn(self):
        # dealer's turn will be different from player's turn per the rules
        pass

    # def end_game(self):
    #     # may need this for player as well???
    #     pass


class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

    def deal_cards(self):
        self.deck.shuffle()

        print(new_game.player)
        card = self.deck.cards.pop()
        self.player.hand.append(card)
        card = self.deck.cards.pop()
        self.player.hand.append(card)
        self.player.view_cards()

        print(new_game.dealer)

        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        card = self.deck.cards.pop()
        self.dealer.hand.append(card)
        self.dealer.view_cards()
        # for card in new_game.dealer.hand:
        #     print(card)
        # need to only show first card in dealer's hand somehow


new_game = Game()
# calls the Game class's init method
new_game.deal_cards()
# tells the game to tell its deck to shuffle itself
