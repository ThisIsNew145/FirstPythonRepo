import random

random_Number = random.randint(1, 10)
guessess = 0
triesLeft = 5
gameOver = False

option = input("This is a number guesser. Do you want to play (it's between 1 to 10)? y/n: ")

if option.lower() == 'y':
    while not gameOver and triesLeft > 0:
        guess = int(input("Guess a number between 1 to 10: "))
        guessess += 1

        if guess == random_Number:
            print("You guessed the number! Well done.")
            print(f'Tries used: {guessess}, Tries left: {triesLeft - 1}')
            gameOver = True
        else:
            triesLeft -= 1
            if triesLeft > 0:
                print("Wrong guess. Try again.")
                print(f'Tries left: {triesLeft}')
            else:
                print("Game over. You used all your tries.")
                print(f"The number was: {random_Number}")
else:
    print("Okay, maybe next time!")

