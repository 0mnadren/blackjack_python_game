def put_money_on_player_account():
    bid_money = input("How much money is on your account: (200$, 300$, 400$, 500$...) ")
    # Checks if input is digit
    while not bid_money.isdigit() or bid_money == '0':
        bid_money = input("How much money is on your account: (200$, 300$, 400$, 500$...) ")
    else:
        return int(bid_money)


def player_bids(player_balance):
    bid = input("How much money are you bidding? ")
    while not bid.isdigit() or player_balance - int(bid) < 0 or bid == '0':
        bid = input(f"Your current balance is {player_balance}$\nHow much money are you bidding? ")
    else:
        return int(bid)


def do_you_Hit_or_Stand():
    question = input("Would you like to HIT or STAND?\n"
                     "Enter 'H' for Hit or 'S' for Stand: ").lower()
    while question != 'h' and question != 's':
        question = input("Would you like to HIT or STAND?\n"
                         "Enter 'h' for Hit and 's' for Stand: ").lower()
    else:
        if question == 'h':
            return 'h'
        elif question == 's':
            return 's'


def keep_playing():
    question = input("Would you like to play another round? Enter ('Y' or 'N') ").lower()
    while question != 'y' and question != 'n':
        question = input("Would you like to play another round? Enter ('Y' or 'N') ").lower()
    else:
        if question == 'y':
            return 'y'
        elif question == 'n':
            return 'n'


"""Functions that prints text when player wins or loses"""
def player_wins_round(name, player_balance, bid):
    print(f"{name} wins this round and gets {bid}$!\n"
          f"{name}'s current balance is {player_balance}$")

def player_loses_round(name, player_balance, bid):
    print(f"{name} loses this round and loses {bid}$!\n"
          f"{name}'s current balance is {player_balance}$")
