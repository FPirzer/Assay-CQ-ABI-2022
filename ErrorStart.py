import random

# List of random range

i = 0
win = 0
while i < 5:
    rng = random.randint(1, 3)
    print(rng)

    i += 1
    try:
        NrGuess = int(input("I think of a number between 1 and 3. Please guess it! "))
        if NrGuess == rng:
            print("You guessed right! Well done. ")
            win += 1
        elif NrGuess != rng:
            print("Sorry but that wasn't the number I thought of! Try again.")
        if NrGuess not in [1, 2, 3]:
            raise RuntimeError("If this is displayed you did something wrong.")
    except RuntimeError:
        print("You have to guess either 1, 2 or 3.")
    except ValueError:
        print("Thats not a number.")
    except:
        break
print(f"You guessed right {win} out of {i} times!")
