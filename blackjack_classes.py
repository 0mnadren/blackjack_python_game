from random import shuffle

signs = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, sign, rank):
        self.sign = sign
        self.rank = rank

    def __str__(self):
        return '--- ' + self.rank + ' of ' + self.sign + ' ---'


# DECK CLASS
class Deck:

    def __init__(self):
        self.new_deck = []
        for sign in signs:
            for rank in ranks:
                self.new_deck.append(Card(sign, rank))

    def shuffle_cards(self):
        shuffle(self.new_deck)

    def deal_card(self):
        """.pop(0) first card from the deck"""
        return self.new_deck.pop(0)

    def __str__(self):
        whole_deck = ''
        for card in self.new_deck:
            whole_deck += '\n' + card.__str__()
        return 'The deck has this cards: ' + whole_deck

    def __len__(self):
        return len(self.new_deck)


# PLAYER CLASS
class Player:

    def __init__(self, name):
        self.name = name
        self.player_cards = []
        self.sums = 0
        self.aces = 0

    def get_card(self, card):
        self.player_cards.append(card)
        self.sums += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def check_for_ace(self):
        while self.sums > 21 and self.aces > 0:
            self.sums -= 10
            self.aces -= 1

    def throw_cards(self):
        self.player_cards.clear()
        self.sums = 0
        self.aces = 0

    def __str__(self):
        print(f"{self.name}'s cards are: ")
        for card in self.player_cards:
            print(card)
        return f'The sum of {self.name}\'s cards is {self.sums}'


class Dealer(Player):
    """INHERITANCE from Class PLAYER"""
    def __init__(self):
        self.name = 'Dealer'
        Player.__init__(self, self.name)


class Account:

    def __init__(self, balance):
        self.balance = int(balance)

    def deposit(self, money):
        self.balance += int(money)

    def lost_money(self, money):
        self.balance -= int(money)

    def __str__(self):
        return self.balance


# test_deck = Deck()
# test_deck.shuffle_cards()
# test_player = Player('Nema')
# test_player.get_card(test_deck.deal_card())
# test_player.get_card(test_deck.deal_card())
# print(test_player.sums)
# for card in test_player.player_cards:
#     print(card)
