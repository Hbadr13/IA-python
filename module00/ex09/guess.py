from random import randrange
ran = randrange(1, 99)
i = 0
print("This is an interactive guessing game!"
    "You have to enter a number between 1 and 99 to find out the secret number.\n"
    "Type 'exit' to end the game.\n"
    "Good luck!")
while True:
    num = input()
    if num == "exit":
        exit(1)
    if num.isdigit() == False:
        print("That's not a number.")
        print("What's your guess between 1 and 99?")
    elif int(num) == ran:
        print("Congratulations, you've got it!")
        print("You won in %d attempts!" % (i))
        exit(1)
    elif int(num) > ran:
        print("Too high!")
    else:
        print("Too low!")
    i = i + 1
