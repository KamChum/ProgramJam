import random

stay = False

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10]
player_total = []
dealer_total = []


#def draw():
#    new_draw = deck[random.randint(0, 8)]
#    return new_draw

def draw(user_total):
    new_draw = deck[random.randint(0, 8)]
    user_total.append(new_draw)
    

def hit():
    new_card = draw()
    
    player_total.append(new_card)

    
    return new_card


def count_total():
    
    total = 0
    for i in player_total:
        total += i

    print(total)
    return total

print("Play Blackjack!")


player_total.append(draw())
player_total.append(draw())

for i in player_total:
    print("Dealt player " + str(i))


total = count_total()
#while under 21 or not stay
while total < 21 and stay == False:

    choice = input("Hit or stay? ")
    if choice == "hit":
        print("Dealt: " + str(hit()))

        total = count_total()
    else:
        stay = True
    
    
    

if total == 21:
    print("Blackjack!")

elif total > 21:
    print("Bust!")
