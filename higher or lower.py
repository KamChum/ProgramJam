import random


num = random.randint(1,5)

choice = int(input("Guess the number! "))

if choice == num:
    print("Guessed right!")
else:
    print("Wrong")
    print("The number was: " + str(num))

