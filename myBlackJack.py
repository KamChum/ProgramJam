import random


#def draw():
#    new_draw = deck[random.randint(0, 8)]
#    return new_draw

def ace(hand):
    if hand == dealer_hand:
        print("Dealer drawn an Ace!")
        if count_total(hand) + 11 > 21:
            return 1
        else:
            return 11
    else:
        choice = input("You've drawn an Ace. Make it 1 or 11? ")
        if choice == "1":
            hand.append(1)
            return 1
        elif choice == "11":
            hand.append(11)
            return 11

def draw(user_total):
    new_draw = deck[random.randint(0, 8)]
    if new_draw == 1:
        return ace(user_total)
    user_total.append(new_draw)
    return new_draw

def count_total(user_total):
    
    total = 0
    for i in user_total:
        total += i

    return total


stay = False

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
player_hand = []
dealer_hand = []


print("Play Blackjack!")


draw(player_hand)
draw(player_hand)

for i in player_hand:
    print("Dealt player " + str(i))

dealer_draw = draw(dealer_hand)
print("Dealer draws: " + str(dealer_draw))
hidden_draw = draw(dealer_hand)

total = count_total(player_hand)
print("Your total: " + str(total))

while total < 21 and stay == False:

    choice = input("Hit or stay? ")
    if choice == "hit":
        print("Dealt: " + str(draw(player_hand)))

        total = count_total(player_hand)
        print("Your total: " + str(total))
    else:
        stay = True

if total == 21:
    print("Blackjack!")

elif total > 21:
    print("Bust!")


print("Hidden card: " + str(hidden_draw))
print("Dealer's total: " + str(count_total(dealer_hand)))
#deal_total = count_total(dealer_hand)
while count_total(dealer_hand) < 18:

    print( "Dealer draws: " + str( draw(dealer_hand) ) )
    print(count_total(dealer_hand))
if count_total(dealer_hand) > 21:
    print("Dealer busts! You win!")

elif count_total(dealer_hand) == 21:
    print("Dealer busts! You win!")

elif count_total(dealer_hand) < count_total(player_hand):
    print("You win!")

elif count_total(dealer_hand) > count_total(player_hand):
    print("You lose!")
