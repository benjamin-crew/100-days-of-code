from blackjack_art import logo
import random
import sys


def start_game():
    """Main game loop"""
    play = input("Would you like to play? Yes/No: ").lower()
    if play == "yes":
        scores_dict['played'] += 1
        deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*16

        # Shuffle deck and assign hands
        random.shuffle(deck)

        player_hand = []
        dealer_hand = []

        for _ in range(2):
            draw_card(player_hand, deck)
            draw_card(dealer_hand, deck)

        play_player(deck, player_hand, dealer_hand)

    # if user does not want to play
    else:
        print("Exiting program")
        print(f"Final Scores: {scores_dict}")
        sys.exit()


def draw_card(hand, deck):
    hand.append(deck.pop(0))

    if sum(hand) > 21 and 11 in hand:
        replace = hand.index(11)
        hand[replace] = 1
        print("11 converted to 1")


def play_player(deck, player_hand, dealer_hand):

    if sum(player_hand) == 21:
        print(f"Your Hand: {player_hand} - Blackjack!")
        play_dealer(deck, player_hand, dealer_hand)

    player_inplay = True
    while player_inplay is True:

        if sum(player_hand) > 21:
            player_inplay = False
            outcome(player_hand)
        else:
            print(f"Your Hand: {player_hand}")
            print(f"Dealers Hand: {dealer_hand[1]}, x")
            draw_or_stick = input("Draw a card or stick? Draw/stick: ").lower()
            if draw_or_stick == "draw":
                draw_card(player_hand, deck)
            elif draw_or_stick == "stick":
                player_inplay = False
                play_dealer(deck, player_hand, dealer_hand)
            else:
                print("Invalid selection")


def play_dealer(deck, player_hand, dealer_hand):

    print(f"Dealers Hand: {dealer_hand} - {sum(dealer_hand)}")

    while sum(dealer_hand) < 17 or sum(dealer_hand) < sum(player_hand):
        draw_card(dealer_hand, deck)

    outcome(player_hand, dealer_hand)


def outcome(player_hand, dealer_hand=""):

    print(
        f"Your hand: {player_hand} - {sum(player_hand)} | {dealer_hand} - {sum(dealer_hand)}")

    if sum(player_hand) > 21:
        print("You bust!")
        scores_dict['losses'] += 1
    elif sum(dealer_hand) > 21:
        print("Dealer busts! You win!")
        scores_dict['wins'] += 1
    elif sum(player_hand) > sum(dealer_hand):
        print("You win!")
        scores_dict['wins'] += 1
    elif sum(player_hand) < sum(dealer_hand):
        print("You lose!")
        scores_dict['losses'] += 1
    elif sum(player_hand) == sum(dealer_hand):
        print("It's a draw!")
        scores_dict['draws'] += 1

    print(scores_dict)
    start_game()


scores_dict = {'played': 0, 'wins': 0, 'losses': 0, 'draws': 0}

print(logo)
start_game()
