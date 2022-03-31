import random

Zahl = random.randint(1, 50)
Possible = False
while not Possible:
    Possible = True
    try:
        Nenner = int(input("Give me a number for the division. "))
        Div = Zahl / Nenner

    except ZeroDivisionError:
        print("Do not divide by zero. Thats how we get black holes.")
    except ValueError:
        Possible = False
        print("Nope. Thats not allowed. Only numbers")
    else:
        print(Div)
