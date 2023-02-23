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

    def deal_card_player(self):
        card = self.cards.pop()
        new_game.player.hand.append(card)

    def deal_card_dealer(self):
        card = self.cards.pop()
        new_game.dealer.hand.append(card)


class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.hand = []

    def __str__(self):
        return f'{self.name} is playing'

    def view_cards(self):
        for card in self.hand:
            print(card)

    def turn(self):
        # player decides how many times to hit before staying
        pass


class Dealer():
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []

    def __str__(self):
        return f'{self.name} is the dealer'
        # will probably not use this, so will delete eventually

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
        print('\nWelcome to Black Jack!\n')
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

    def deal_cards(self):
        self.deck.shuffle()

        # print(new_game.player)

        self.deck.deal_card_player()
        self.deck.deal_card_player()

        self.deck.deal_card_dealer()
        self.deck.deal_card_dealer()

        print("\n" + self.dealer.name + "'s Cards:")
        self.dealer.view_cards()

        print("\n" + self.player.name + "'s Cards:")
        self.player.view_cards()
        # need to only show first card in dealer's hand somehow; make new function and rename view_cards to reveal_cards???


new_game = Game()
# calls the Game class's init method
new_game.deal_cards()
# tells the game to tell its deck to shuffle itself
