import random


name = input("Enter your name: ")
question = "Will I die from being eaten by a zombie horde?"
answer = ""

while True:
    random_number = random.randint(1, 9)
    if random_number == 1:
        answer = "Yes - salted and peppered"
    elif random_number == 2:
        answer = "It is decidedly so - call mommy and say goodbye"
    elif random_number == 3:
        answer = "Without a doubt - you are the slowest runner in the group"
    elif random_number == 4:
        answer = "Reply hazely, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "No - you don't look tasty"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    else:
        answer = "Error"

    print(name, "asks:", question, "\n")
    print("Magic 8-Ball's answer:", answer)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break