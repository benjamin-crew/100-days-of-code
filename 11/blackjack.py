from blackjack_art import logo
import random
import sys

def sum_of_list(list):
    list_sum = 0
    for n in list:
        list_sum += n
    
    return list_sum


def start_game():
    """This function starts the game and asks if you would like to play"""
    play = input("Would you like to play? Yes/No: ").lower()
    if play == "yes":
        initialise_deck()
    else:
        sys.exit()


def initialise_deck():
    """This function creates the deck and shuffles it."""
    suit_template = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    four_suits = suit_template + suit_template + suit_template + suit_template
    deck = (four_suits + four_suits + four_suits + four_suits)
    print("Shuffling the deck...")
    random.shuffle(deck)
    #add if statement if games_played = n, shuffle deck

    play_hands(deck)


def play_hands(deck):
    """Main play loop"""
    player_hand = []
    dealer_hand = []

    player_hand.append(deck.pop(0))
    dealer_hand.append(deck.pop(0))

    player_hand.append(deck.pop(0))
    dealer_hand.append(deck.pop(0))

    print(f"Your Hand: {player_hand}")
    print(f"Dealers Hand: {dealer_hand[1]}, x")
    
    play_player(deck, player_hand, dealer_hand)


def play_player(deck, player_hand, dealer_hand):

    player_inplay = True

    print(f"Your hand: {player_hand} - {sum_of_list(player_hand)}")

    while player_inplay is True:
        while sum(player_hand) > 21 and 11 in player_hand:
                replace = player_hand.index(11)
                player_hand[replace] = 1

        if sum(player_hand) > 21:
                print("You lose!")
                player_inplay = False
                sys.exit()
        else:
            draw_or_stick = input("Draw a card or stick? Draw/stick: ").lower()
            if draw_or_stick == "draw":
                player_hand.append(deck.pop(0))
                print(f"You draw a {player_hand[-1]}")
                print(f"Your hand: {player_hand} - {sum_of_list(player_hand)}")
            elif draw_or_stick == "stick":
                player_inplay = False
                play_dealer(deck, player_hand, dealer_hand)
            else:
                print("Invalid selection")
                sys.exit()
    
def play_dealer(deck, player_hand, dealer_hand):

    print(f"Dealers Hand: {dealer_hand} - {sum_of_list(dealer_hand)}")

    while sum_of_list(dealer_hand) < 17:
        if sum_of_list(dealer_hand) >= 17:
            dealer_inplay = False
            winner()
        else:
            if sum_of_list(dealer_hand) >= sum_of_list(player_hand) and sum_of_list(dealer_hand) <= 21:
                if sum_of_list(dealer_hand) == sum_of_list(player_hand):
                    print(f"Your hand: {player_hand} - {sum_of_list(player_hand)} | {dealer_hand} - {sum_of_list(dealer_hand)}")
                    print("It's a draw!")
                else:
                    print(f"Your hand: {player_hand} - {sum_of_list(player_hand)} | {dealer_hand} - {sum_of_list(dealer_hand)}")
                    print("Dealer wins.")
                    dealer_inplay = False
                    sys.exit()
            elif sum_of_list(dealer_hand) <= sum_of_list(player_hand) and sum_of_list(dealer_hand) < 17:
                dealer_hand.append(deck.pop(0))
                print(f"The dealer draws a {dealer_hand[-1]}")
            else:
                print(f"Your hand: {player_hand} - {sum_of_list(player_hand)} | {dealer_hand} - {sum_of_list(dealer_hand)}")
                print("You win!")
                sys.exit()

def winner(player_hand, decker_hand):

### figure out dealer section and winner
# 	if on 17, don’t draw anymore
# 	get more than player
	
# 		if over 21 and has 11, change 11 to 1
# 	bust
	
	

print(logo)
start_game()