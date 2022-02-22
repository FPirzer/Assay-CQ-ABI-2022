import random

# List of random range
rng = random.randint(0, 99)
print(rng)
GuessRight = False
i = 0
while GuessRight == False:
    NrGuess = input("I think of a number. Please guess it! ")
    if NrGuess.isdigit():
        NrGuess = int(NrGuess)
        if NrGuess > rng:
            print("Your number is too big. Try again! ")
            i += 1
        elif NrGuess < rng:
            print("Your number is small big. Try again! ")
            i += 1
        else:
            GuessRight = True
            if i < 1:
                print("You cheater. On the first try!")
            else:
                print("You found the number! It only took you ", i, "tries.")

    else:
        print("Your input wasn't a positiv number!")
