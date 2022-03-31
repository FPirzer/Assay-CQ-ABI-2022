"""
This si the GUi I created for talking about text field during our Course on the
28.2.2022. This program creates atext field, 3 Buttons and a Label. Each button
has a specific function associated with it, that works on the text field. Even
though this example script only contains three buttons and one Label it can work
as a kind of muster soltuion for exercise 13. Since nearly all the needed
functions are present in this program. Only the inserting text at the end is
missing, but since this is just an adjustment of the position inside the insert
command that is seen in Text_Output() function that shouldn't be that difficult.
For showing which button was pressed last you just have to add a second label,
e.g. label2, to your GUI and include one line as shown below to your functions:
self.label2.config(text="Button1 was pressed")
This simple line is all you need in all your functions, of course you have to
change the string after text= accordingly.
"""
# First we import our tkinter module
import tkinter as tk

# Now we define our class as we saw multiple times last week.
class Editor:
    # Now we generate our contructor to set up our GUI
    def __init__(self):
        # First we create our root, so that we can put all remaining widgets
        # in it.
        self.root = tk.Tk()
        # Than we create our text field witht he help of tk.Text(), we only hand
        # over the parent, the root in our case, to it
        self.text1 = tk.Text(self.root)
        # Now we pack it into our GUI
        self.text1.pack()
        # Next we create the three Buttons that are needed for the different
        # functions we want to be able doing during the run of our program.
        # Each button isn't formatted in any kind of way and is only associated
        # with a simple function. The first on is used to insert text into our
        # field later on and than print out the text into the terminal
        self.button1 = tk.Button(
            self.root, text="get Contents", command=self.Text_Output
        )
        # We pack the button at the left side of our GUI under our text field
        self.button1.pack(side="left")
        # The second button is used to clear our text field later on.
        self.button2 = tk.Button(
            self.root, text="clear Text field", command=self.Text_Clear
        )
        # We pack the button on the right side of our GUI under our text field
        self.button2.pack(side="right")
        # The thrid button is used to get the length ouf our text and print the
        # result in a Label.
        self.button3 = tk.Button(
            self.root, text="Display Text length", command=self.Text_length
        )
        # We pack the button at the bottom of GUI, in the center
        self.button3.pack(side="bottom")
        # Now we create the Labe that is needed to display the length of our
        # text witht he help of button3
        self.label1 = tk.Label(self.root, text="")
        # We also pack this Label at the bottom of our GUI
        self.label1.pack(side="bottom")
        # Last but not least we start the mainloop to get our GUI running.
        self.root.mainloop()

    # Now we can define our three functions that are needed to get our GUI
    # working. First we define the function for button1 to insert something in
    # our text field and than print out the whole text into our terminal. As you
    # can see below all functions take only the class itself as an argument.
    # That's why we didn't need to use lambda in the command argument earlier on
    def Text_Output(self):
        # First we insert something. This can be done by using the insert method
        # with two arguments. The first is the position were you want to enter
        # something and the second is the string you want to enter. In the case
        # seen here we want to insert something in line1 and character 0.
        self.text1.insert(1.0, "This is a Test\n")
        # Now we read in the contents of our text field. I created a variable
        # here but you could use the get method directly in the print command as
        # well. The get method always works with 2 arguments, the start and end
        # position of the text you want to read in. We use the special position
        # "end" in this example. "end" always refers to the last position in the
        # text. Keep in mind that tkinter always adds a linebreak at the end of
        # your text.
        self.Content = self.text1.get(1.0, "end")
        # Now we can print out the text into our terminal. As we already saw
        # when we were working with files, print interprets the line breaks, so
        # you get a print out that loosk exactly as it's in the text field.
        print(self.Content)
        # I included the repr method here to show you how your string really
        # looks like after you read him in.
        print(repr(self.Content))

    # The next function we want to create is a pretty simple one. This function
    # should clear the text field completely.
    def Text_Clear(self):
        # We can delete the whole text with the delete function and two
        # positions as arguments, similiar to get. Everything between the two
        # positions is than deleted. In the example here we use the position 1.0
        # to get the very first letter and the position end to even include the
        # unwanted line break at the end.
        self.text1.delete(1.0, "end")

    # Our last functions should read in the text again and give us the number of
    # characters in our text field. I created a "one-line" function here to show
    # you that you don't need a variable to read in the value of a text field.
    # For an entry field this wouldn't be possible since we always need a VarVar
    # that is associated with it.
    def Text_length(self):
        # Since we want to display the lenght of our text in the label we added
        # earlier we have to use the config method of our label to change the
        # text in it. I used the + signs to put together a more complex text
        # here. First we have a simple statement, than after the first + we read
        # in the text of our text field with get(), calculate the length of the
        # resulting string with len() and cast the result (an int) to a String
        # with str(). Afterward we add another simple statement with a + and
        # finish our config. As you can see I used "end-1c" as a position to
        # ignore the last character (the automatically added line break). You
        # can even use "end-1l", "end-2l" or "end-3c" to ignore the last line,
        # the last two lines or the last three characters respectively.
        # Please note that each line break in your text is counted as one
        # character.
        self.label1.config(
            text="You're text has "
            + str(len(self.text1.get(1.0, "end-1c")))
            + " characters"
        )


# Last but not least we initiate our GUI.
Editor()
