###############################################
# APS106 Winter 2020 - Lab 5 - Card Game      #
###############################################

import random


#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    cards = []
    suits = ['spades', 'clubs', 'diamonds', 'hearts']

    for suit in suits:
        for number in range(1, 14):
            cards.append([suit, number])

    return cards


def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of the deck of cards

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck, len(deck))

    return shuffled_deck


####################################################
# PART 1 - Complete the following helper functions
#          that will be used to create our game
####################################################

def deal_card(deck, hand):
    """
    (list,list) -> None

    Deal a card from the first element in the deck list and add it to the list
    representing the player's hand

    """

    ## TODO YOUR CODE HERE
    hand.append(deck[0])
    deck.remove(deck[0])


def score_hand(hand):
    """
    (list) -> int

    Calculate the score of the player's hand. Points for each card are
    calculated as follows:
        Face Cards (jack,queen,king) = 10 points
        Number Cards = face value (i.e. a 2 would be worth 2 points, a 6 would
          be worth 6 points)
        Ace = Either 1 or 11 points depending what gives the hand a higher
          score without going over 21

    """

    ## TODO YOUR CODE HERE
    points = 0
    ace = False
    ace_counter = 0
    for cards in hand:
        if 2 <= cards[1] <= 10:
            points += cards[1]
        elif 11 <= cards[1] <= 13:
            points += 10
        elif cards[1] == 1:
            print("ace found")
            ace = True
            ace_counter += 1

        else:
            points += 0

    if ace:
        for i in range(ace_counter):
            if (points + 11) > 21:
                points += 1
            else:
                points += 11

    return points


###############################################
# Part 2 - Write the Function that executes
#          the game using the helper functions
###############################################

def play(shuffled_deck):
    """
    (list) -> list

    Play our game and return a list containing the following elements:
        winner - str indicating the winner, either "player" or "dealer"
        winner_hand - list containing the cards in the winner's hand
        loser_hand - list containing the cards in the loser's hand

    """

    # define the player and dealer hands
    player_hand = []
    dealer_hand = []

    ## TODO YOUR CODE HERE
    # Deal the cards
    deal_card(shuffled_deck, player_hand)
    deal_card(shuffled_deck, dealer_hand)
    deal_card(shuffled_deck, player_hand)
    deal_card(shuffled_deck, dealer_hand)

    done = False  # checks to see if game is done

    while not done:

        if score_hand(player_hand) < 15:
            deal_card(shuffled_deck, player_hand)
            if score_hand(player_hand) > 21:
                # Dealer wins
                return ["dealer", dealer_hand, player_hand]
                done = True

        elif len(dealer_hand) < 3:
            deal_card(shuffled_deck, dealer_hand)
            if score_hand(dealer_hand) > 21:
                # Player wins
                return ["player", player_hand, dealer_hand]
                done = True

        # Check to see if you have to run the loop again
        elif score_hand(player_hand) < 15 or len(dealer_hand) < 3:
            done = False
        else:
            if score_hand(player_hand) > score_hand(dealer_hand):
                # Player wins
                return ["player", player_hand, dealer_hand]
                done = True
            else:
                # Dealer wins
                return ["dealer", dealer_hand, player_hand]
                done = True


print(score_hand([['hearts', 1], ['spades', 8], ['clubs', 4]]))