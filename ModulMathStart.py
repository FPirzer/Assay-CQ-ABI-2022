import math

print("1. Exp")
print("2. Log")
print("3. Log2")
print("4. Log10")
print("5. Pow")
print("6.Sqrt")
print("7. Cos")
print("8. Sin")
print("9. Tan")
print("10. Acos")
print("11. Asin")
print("12. Atan")

ValidChoice = True
while ValidChoice:
    Choice = input("What math operation do you want to use? ")
    if Choice.isdigit():
        Choice = int(Choice)
        if Choice > 12 or Choice < 1:
            print("This is not a valid choice")
        elif Choice > 1 and Choice < 12:
            ValidChoice = False
    else:
        print("Your input wasn't a positiv number!")


Nr1accept = False
while not Nr1accept:
    Nr1 = input("The first number for the calculation: ")
    if Nr1.isdigit():
        Nr1 = int(Nr1)
        if (Choice == 2 or Choice == 3 or Choice == 4) and Nr1 <= 0:
            print("This is not a valid choice for the Log funtion")
        elif (Choice == 10 or Choice == 11 or Choice == 12) and (Nr1 < -1 or Nr1 > 1):
            print("This is not a valid choice for the arcus funtions")
        else:
            Nr1accept = True
    else:
        print("Your input wasn't a number!")
if Choice == 2 or Choice == 5:
    Nr2accept = False
    while not Nr2accept:
        Nr2 = input("The second number for the calculation: ")
        if Nr2.isdigit():
            Nr2 = int(Nr2)
            if (Choice == 2 or Choice == 3 or Choice == 4) and Nr2 <= 0:
                print("This is not a valid choice for the Log funtion")
            elif (Choice == 10 or Choice == 11 or Choice == 12) and (
                Nr2 < -1 or Nr2 > 1
            ):
                print("This is not a valid choice for the arcus funtions")
            else:
                Nr2accept = True
        else:
            print("Your input wasn't a number!")

# math.pi
# math.e
# math.tau


print("Exp:", math.exp(Nr1))
print("Log:", math.log(Nr1, Nr2))
print("Log2:", math.log2(Nr1))
print("Log10:", math.log10(Nr1))
print("Pow:", math.pow(Nr1, Nr2))
print("Sqrt:", math.sqrt(Nr1))
print("Cos:", math.cos(Nr2))
print("Sin:", math.sin(Nr2))
print("Tan:", math.tan(Nr2))
print("acos:", math.acos(Nr2))
print("asin:", math.asin(Nr2))
print("atan:", math.atan(Nr2))
