from blackjack_classes import Deck, Player, Dealer, Account
from blackjack_functions import put_money_on_player_account, player_bids, player_wins_round
from blackjack_functions import player_loses_round, do_you_Hit_or_Stand, keep_playing
from time import sleep


# GAME SETUP
gameOn = True
player_name = input("Player's name: ")
player = Player(player_name.title())  # Creates Player
money_on_player_account = put_money_on_player_account()  # Starting balance
player_account = Account(money_on_player_account)  # Creates Player Account
dealer = Dealer()  # Creates DEALER
deck = Deck()  # Creates DECK
deck.shuffle_cards()  # Shuffles DECK


# GAME INIT
while gameOn:

    player_bid = player_bids(player_account.balance)  # Player's bid amount

    # Player gets 2 cards:
    player.get_card(deck.deal_card())
    player.get_card(deck.deal_card())
    print(player)
    sleep(1)

    # Dealer gets 1 card:
    dealer.get_card(deck.deal_card())
    print(dealer)
    sleep(0.5)

    if player.sums == 21:
        player_account.deposit(player_bid)
        player_wins_round(player.name, player_account.balance, player_bid)
        player.throw_cards()
        dealer.throw_cards()
        sleep(1)
    else:
        # Ask player if he want to HIT or STAND
        player_hit_or_stand = True
        while player_hit_or_stand:
            hit_or_stand = do_you_Hit_or_Stand()
            if hit_or_stand == 'h':
                player.get_card(deck.deal_card())
                player.check_for_ace()
                print(player)
                sleep(1)
                if player.sums >= 21:
                    player_hit_or_stand = False
            elif hit_or_stand == 's':
                player_hit_or_stand = False

        # Dealers round to draw cards
        if player.sums <= 21:
            while dealer.sums < 17:
                dealer.get_card(deck.deal_card())
                print(dealer)
                sleep(1)

        # Win conditions
        if player.sums == 21 and dealer.sums != 21:
            player_account.deposit(player_bid)
            player_wins_round(player.name, player_account.balance, player_bid)
            player.throw_cards()
            dealer.throw_cards()
            sleep(1)

        elif player.sums == dealer.sums:
            print("No one wins, it's a tie!\n"
                  f"{player.name}'s current balance is {player_account.balance}$")
            player.throw_cards()
            dealer.throw_cards()
            sleep(1)

        elif player.sums != 21 and dealer.sums == 21:
            player_account.lost_money(player_bid)
            player_loses_round(player.name, player_account.balance, player_bid)
            player.throw_cards()
            dealer.throw_cards()
            sleep(1)

        elif player.sums < 21 < dealer.sums:
            player_account.deposit(player_bid)
            player_wins_round(player.name, player_account.balance, player_bid)
            player.throw_cards()
            dealer.throw_cards()
            sleep(1)

        elif player.sums > 21:
            player_account.lost_money(player_bid)
            print('BUST!')
            player_loses_round(player.name, player_account.balance, player_bid)
            player.throw_cards()
            dealer.throw_cards()
            sleep(1)

        elif player.sums < 21 and dealer.sums < 21:
            if player.sums > dealer.sums:
                player_account.deposit(player_bid)
                player_wins_round(player.name, player_account.balance, player_bid)
                player.throw_cards()
                dealer.throw_cards()
                sleep(1)
            elif player.sums < dealer.sums:
                player_account.lost_money(player_bid)
                player_loses_round(player.name, player_account.balance, player_bid)
                player.throw_cards()
                dealer.throw_cards()
                sleep(1)

    if player_account.balance == 0:
        gameOn = False
        print('GameOver! Thanks for playing with us!')
        break

    playing = keep_playing()
    if playing == 'n':
        gameOn = False
        print('Thanks for playing with us!')

















