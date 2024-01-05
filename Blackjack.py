import random

player_in = True
dealer_in = True

# deck of cards & player/dealer hands
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
player_hand = []
dealer_hand = []

# dealing
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculating total of player/dealer hands
def total(player_hand):
    total = 0
    ace_11 = 0
    for card in player_hand:
        if card in range(11):
            total += card
        elif card in ['J', 'Q', 'K']:
            total += 10
        else:
            total += 11
            ace_11 += 1
    while ace_11 and total > 21:
        total -= 10
        ace_11 -= 1
    return total

if total(player_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("BLACKJACK --- You win")
elif total(dealer_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("BLACKJACK --- Dealer wins")
# winner
def showDealersHand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

# game loop
for _ in range(2):
    dealCard(dealer_hand)
    dealCard(player_hand)

while player_in or dealer_in:
    print(f"Dealer's hand: {showDealersHand()} and X")
    print(f"Your hand: {player_hand} for a total of {total(player_hand)}")
    if player_in:
        stayHit = input("Stay or hit?")
    if total(dealer_hand) > 17:
        dealer_in = False
    else:
        dealCard(dealer_hand)
    if stayHit == "stay":
        player_in = False
    else:
        dealCard(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

# determine winner
if total(player_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("BUST --- Dealer wins")
elif total(dealer_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("BUST --- You win")
elif 21 - total(dealer_hand) < 21 - total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer wins")
elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You win")




