import random

SUITS = ['♥️', '♣️', '♠️', '♦️']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit=None, rank=None):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank}{self.suit}'


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

    def deal_opening_hands(self):
        self.shuffle()
        # shuffle the deck
        self.deal_card_player()
        self.deal_card_player()
        # deal two cards to the player
        self.deal_card_dealer()
        self.deal_card_dealer()
        # deal two cards to the dealer

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
        self.score = 0

    def __str__(self):
        return f'{self.name} is playing'

    def view_cards(self):
        for card in self.hand:
            print(card)

    def calculate_score(self):
        pass

    def turn(self):
        # player decides how many times to hit before staying
        pass


class Dealer():
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
        self.score = 0

    def __str__(self):
        return f'{self.name} is the dealer'
        # will probably not use this -- may delete eventually

    def view_cards_start(self):
        for card in self.hand:
            if card == self.hand[0]:
                print("???")
            else:
                print(card)

    # How do I make the cards print horizontally instead of vertically???

    def view_cards(self):
        for card in self.hand:
            print(card)

    def calculate_score(self):
        pass

    def turn(self):
        # dealer's turn will be different from player's turn per the rules
        pass


class Game:
    def __init__(self):
        print('\nWelcome to Black Jack!\n')
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

    # Pretty sure this entire method should be in the deck class
    def deal_cards(self):
        self.deck.deal_opening_hands()

        print("\n" + self.dealer.name + "'s Cards:")
        self.dealer.view_cards_start()
        # show dealers hand
        # make new Dealer method reveal_cards???
        print("\n" + self.player.name + "'s Cards:")
        # print(self.player.hand)
        # how do I make the cards show side-by-side instead of printed one at a time???
        self.player.view_cards()
        # show player's hand


new_game = Game()
# calls the Game class's init method
new_game.deal_cards()
# tells the game to tell its deck to shuffle itself

# CHECK TO SEE IF DEALER HAS 21
# CHECK TO SEE IF PLAYER HAS 21
# END GAME IF EITHER/BOTH HAVE 21

# PLAYER TURN
# DEALER TURN
