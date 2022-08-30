import random

# deck of cards / player dealer hand
deck = [2, 3, 4, 5 ,6, 7, 8, 9, 10, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
player_hand = []
dealer_hand = []
# deal the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand

# check for winner

# game loop