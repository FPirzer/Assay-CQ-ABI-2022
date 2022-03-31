# The parameter "w" gives writting access to the file regardless of content aka overwritting
Text = open("Writting-Test.txt", "w")
Text.write("This is a one liner!\n")
Text.write("I forgot the second line. Duh!\n")
Text.close()
# The parameter "a" append to the end of the file and DON'T overwrite the content
Text = open("Writting-Test.txt", "a")
Text.write("A third line to append to the established text file.\n")
Text.write("And another one.\n")
Text.close()

with open("Countdown.txt", "w") as Countdown:
    for i in reversed(range(11)):
        Countdown.write(str(i) + "\n")

# Count the content of the countdown.txt
# with open("Countdown.txt", "r") as Countdown:
#     Final = Countdown.readlines()
#     Summe = 0
#     for i in Final:
#         i = int(i)
#         Summe += i
# print("Summe:", Summe)

with open("Countdown.txt", "r") as Countdown:
    NewText = input("Name the new Textfile: ") + ".txt"
    with open(NewText, "w") as New:
        for lines in Countdown:
            New.write(lines)
    print(NewText)
