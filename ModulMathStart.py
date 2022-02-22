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

Falsechoice = True
while Falsechoice:
    Choice = input("What math operation do you want to use? ")
    if Choice.isdigit():
        Choice = int(Choice)
        if Choice > 12 or Choice < 1:
            print("This is not a valid choice")
        elif Choice > 1 and Choice < 12:
            Falsechoice = False
    else:
        print("Your input wasn't a positiv number!")


Nr1 = input("The first number for the calculation: ")
if Nr1.isdigit():
    Nr1 = int(Nr1)
    if Choice == 2 and Nr1 <= 0:
        print("This is not a valid choice for the Log funtion")
else:
    print("Your input wasn't a number!")

# Dont want to implement all the exeptions -.-

Nr2 = input("The second number for the calculation: ")
if Nr2.isdigit():
    Nr2 = int(Nr2)
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
