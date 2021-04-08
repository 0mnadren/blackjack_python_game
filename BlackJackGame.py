from random import shuffle
from time import sleep

# todo: Go over the rules of the game, change if needed!
znak = ('Tref', 'Pik', 'Herz', 'Karo')
rangs = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
         'Queen', 'King', 'Ace')
vrednost = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
            'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
            'Queen': 10, 'King': 10, 'Ace': 11}


# DECK CLASS
class Deck:
    """Deck Class"""
    def __init__(self):
        self.mark = znak
        self.rang = rangs
        self.new_deck = []
        for rang in self.rang:
            self.value = vrednost[rang]

    def make_deck(self):
        """Creates a deck"""
        for mark in self.mark:
            for num in self.rang:
                self.new_deck.append(num + ' ' + mark)
        # print(self.new_deck)
        return self.new_deck

    def shuffle_cards(self):
        """Function shuffles the deck"""
        shuffle(self.new_deck)

    def deal_card(self):
        """.pop(0) first card from the deck"""
        return self.new_deck.pop(0)


# PLAYER CLASS
class Player:
    """Player Class
        Has name / player_cards(hand_cards) / sum of player's HAND"""
    def __init__(self, name):
        self.name = name
        self.player_cards = []
        self.sums = 0

    def get_cards(self, cards):
        return self.player_cards.append(cards)

    def restart_sum(self):
        self.sums = 0
        return self.sums

    def sum_of_cards(self, hand_cards):
        """Creates one string from list hand_cards
        Splits created string into list
        Loop through a list and GETS SUM of HAND"""
        self.sums = 0
        make_string = ' '.join(hand_cards)
        split_card_name = make_string.split()
        for card in split_card_name:
            if card in vrednost.keys():
                self.sums += vrednost[card]
            else:
                continue

        return self.sums

    def get_rang(self, hand_cards):  # todo: Implement this to check for ACES in Player's hand
        make_string = " ".join(hand_cards)
        split_card_name = make_string.split()
        for index, rang in enumerate(split_card_name):
            if index % 2 == 0:
                return rang
            else:
                continue

    def del_list(self):
        self.player_cards.clear()
        return self.player_cards

    def __str__(self):
        return f"{self.name}'s cards are: {self.player_cards}\n" \
               f'Sum is: {self.sums}'


# CLASS DEALER
class Dealer(Player):
    """INHERITANCE from Class PLAYER"""
    def __init__(self):
        self.name = 'Dealer'
        Player.__init__(self, self.name)


# CLASS ACCOUNT
class Account:

    def __init__(self, balance):
        self.balance = int(balance)

    def deposit(self, money):
        """ADDS money in self.balance"""
        self.balance += int(money)
        return self.balance

    def lost_money(self, money):
        """REMOVES money from self.balance"""
        self.balance -= int(money)
        return self.balance

    def __str__(self):
        return f'On you account you have {self.balance}$'


# GAME SET UP

name_of_player = input("Player's name: ")
bid_money = input("How much money is on your account: (200$, 300$, 400$, 500$...) ")
player1 = Player(name_of_player)  # Creates PLAYER1

# Checks if player entered a number and not something else
while not bid_money.isdigit():
    bid_money = input("How much money is on your account: (200$, 300$, 400$, 500$...) ")
else:
    player1_account = Account(bid_money)

dealer = Dealer()  # Creates DEALER
deck_of_cards = Deck()  # Creates DECK OBJECT
deck_of_cards.make_deck()  # Creates DECK
deck_of_cards.shuffle_cards()  # Shuffles DECK
rounds = 0
player_balance = player1_account.balance

# Check if PLAYER has money in ACCOUNT
while player_balance > 0:

    if rounds == 0:
        round_bid = input("How much money are you bidding? ")
        while not round_bid.isdigit():
            round_bid = input("How much money are you bidding? ")
        else:
            while player_balance - int(round_bid) < 0:
                round_bid = input(f"Your current balance is {player_balance}\nHow much money are you bidding? ")

        player1.restart_sum()
        dealer.restart_sum()
        player1.get_cards(deck_of_cards.deal_card())
        print(player1)
        player1.get_cards(deck_of_cards.deal_card())
        player_sum = player1.sum_of_cards(player1.player_cards)
        print(player1)
        sleep(1)

        dealer.get_cards(deck_of_cards.deal_card())
        print(dealer)
        dealer.get_cards(deck_of_cards.deal_card())
        dealer_sum = dealer.sum_of_cards(dealer.player_cards)

        if player_sum == 21:
            player_balance = player1_account.deposit(round_bid)
            print(f"{name_of_player} wins this round and gets {round_bid}$!\n"
                  f"{name_of_player}'s current balance is {player_balance}$")
            player1.del_list()
            dealer.del_list()
            sleep(2)
        else:
            rounds += 1
    elif rounds != 0:

        player_draw = True
        while player_draw:
            continue_playing = input('Do you want to draw a card? (Y or N) ')
            if continue_playing.upper() == 'Y':
                player1.restart_sum()
                player1.get_cards(deck_of_cards.deal_card())
                player_sum = player1.sum_of_cards(player1.player_cards)
                print(player1)
                rounds = 0
                sleep(1)
                if player_sum >= 21:
                    player_draw = False
                else:
                    continue

            elif continue_playing.upper() == 'N':
                player_draw = False
        else:
            print(dealer)
            sleep(0.7)
            # IF DEALER HAS HIS SUM OF HAND < 17 GETS MORE CARDS
            while dealer_sum < 17:
                dealer.restart_sum()
                dealer.get_cards(deck_of_cards.deal_card())
                dealer_sum = dealer.sum_of_cards(dealer.player_cards)
                print(dealer)
                sleep(1.5)

            else:
                player_draw = False
                sleep(1.5)

        # LONG CHECKS OF WIN CONDITIONS
        if player_sum == 21 and dealer_sum < 21 < dealer_sum:
            player_balance = player1_account.deposit(round_bid)
            print(f"{name_of_player} wins this round and gets {round_bid}$!\n"
                  f"{name_of_player}'s current balance is {player_balance}$")
            rounds = 0
            player1.del_list()
            dealer.del_list()
            sleep(1.5)
        elif player_sum < 21 < player_sum and dealer_sum == 21:
            player_balance = player1_account.lost_money(round_bid)
            print(f"{name_of_player} losses this round and losses {round_bid}$!\n"
                  f"{name_of_player}'s current balance is {player_balance}$")
            rounds = 0
            player1.del_list()
            dealer.del_list()
            sleep(1.5)
        elif player_sum == 21 and dealer_sum == 21:
            print("No one wins, it's a tie!\n"
                  f"{name_of_player}'s current balance is {player_balance}$")
            rounds = 0
            player1.del_list()
            dealer.del_list()
            sleep(1.5)
        elif player_sum < 21 < dealer_sum:
            player_balance = player1_account.deposit(round_bid)
            print(f"{name_of_player} wins this round and gets {round_bid}$\n"
                  f"{name_of_player}'s current balance is {player_balance}$")
            rounds = 0
            player1.del_list()
            dealer.del_list()
            sleep(1.5)
        elif player_sum > 21:
            player_balance = player1_account.lost_money(round_bid)
            print(f"BUST! {name_of_player} losses this round and losses {round_bid}$!\n"
                  f"{name_of_player}'s current balance is {player_balance}$")
            rounds = 0
            player1.del_list()
            dealer.del_list()
            sleep(1.5)
        elif player_sum < 21 and dealer_sum < 21:
            if player_sum > dealer_sum:
                player_balance = player1_account.deposit(round_bid)
                print(f"{name_of_player} wins this round and gets {round_bid}$\n"
                      f"{name_of_player}'s current balance is {player_balance}$")
                rounds = 0
                player1.del_list()
                dealer.del_list()
                sleep(1.5)
            elif player_sum < dealer_sum:
                player_balance = player1_account.lost_money(round_bid)
                print(f"{name_of_player} losses this round and losses {round_bid}$!\n"
                      f"{name_of_player}'s current balance is {player_balance}$")
                rounds = 0
                player1.del_list()
                dealer.del_list()
                sleep(1.5)
            else:
                print("No one wins, it's a tie!\n"
                      f"{name_of_player}'s current balance is {player_balance}$")
                rounds = 0
                player1.del_list()
                dealer.del_list()
                sleep(1.5)

else:
    print('Game is over! Thanks for playing with us!')














