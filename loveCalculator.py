import time
import random

print("Love Calculator!\n")

name_one = input("First lover's name: ")

name_two = input("Second lover's name: ")

print("Calculating...\n")
time.sleep(2)
result = random.randint(0, 100)

if name_one == "Kamil" and name_two == "Tasha" or name_one == "Tasha" and name_two == "Kamil":
    print("Compatibility is over 9000!")
else:
    print(str(result) + "% compatible!")

    if result >= 80:
        print("Star-crossed lovers!")
    elif result >= 50:
        print("You could make it work!")
    else:
        print("It wouldn't work out..")