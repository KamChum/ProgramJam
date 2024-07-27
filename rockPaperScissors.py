import time
import random


def game():
    rps_list = ["rock", "paper", "scissors"]

    print("rock paper scissors!\n")

    choice = input("rock, paper, or scissors? ")

    for i in range(1, 3):
        print(i)
        time.sleep(1)

    cpu_choice = rps_list[random.randint(0,2)]

    print("Opponent picked: " + str(cpu_choice))

    if choice == "rock" and cpu_choice == "scissors":
        print("you win!")
    elif choice == "scissors" and cpu_choice == "rock":
        print("you lose!")
    elif choice == "paper" and cpu_choice == "rock":
        print("you win!")
    elif choice == "rock" and cpu_choice == "paper":
        print("you lose!")
    elif choice == "scissors" and cpu_choice == "paper":
        print("you win!")
    elif choice == "paper" and cpu_choice == "scissors":
        print("you lose!")
    else:
        print("draw!")

    play_again()


def play_again():
    if input("Play again? y/n ") == "y":
        game()


game()