"""
This is the example script for working with option menus. This script shows you
a simpel example for working with these widgets. The layout of our GUIs don't
really matter at the moment so bear with the rather plain look of them. The
function that is included at the bottom of our class definition can be seen as
a Blueprint for the functions you need in exercise 14. You just have to change
the part in the brackets of the config method. I included one small example for
setting the background color.
"""
# First we import tkinter as always
import tkinter as tk


# Now we define our class Options to be able to generate our GUI
class Options:
    # Now we set up our Contructor.
    def __init__(self):
        # First we have to define our root.
        self.root = tk.Tk()
        # I included a new method in this script. The geometry method can be
        # used to define the dimensions of your GUI at the start of it. The
        # syntax is pretty simple, as you have to include the wanted dimensions
        # as a string inside the brackets. The first number represents the width
        # and the second number represents the height.
        self.root.geometry("500x200")
        # For each menu we have to define a VarVar that is associated with it,
        # so we can later access the chosen value. I used StringVars here
        # because we can hand them over to our configs later on.
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        # Now I define the start values of our VarVars with set(). The menus we
        # create afterwards will them be able to display the chosen start value
        # directly on the start up of our GUI.
        self.var1.set("Option 1")
        self.var2.set("snow")
        # Now we define our two menus. We have to hand over several attributes
        # to them so that they can work. First we define the parent, than we
        # hand over the VarVar that is associated with the menu, in this case
        # var1. Afterwards we add the wanted options as strings, separated by
        # Commas. Last but not least we add a function that is associated with
        # our menu. For the first one that is the function display selected.
        self.menu = tk.OptionMenu(
            self.root,
            self.var1,
            "Option 1",
            "Option 2",
            "Option 3",
            command=self.display_selected,
        )
        # Now we pack our menu on hte left side of our GUI to make it visible.
        self.menu.pack(side="left")
        # Now we can create another menu. This menu is associated with var2,
        # contains some colors and is associated with the function change_bg.
        self.menu2 = tk.OptionMenu(
            self.root, self.var2, "blue", "snow", "grey", command=self.change_bg,
        )
        # We again pack it to the left side of our GUI and it's now on the right
        # side of the first one, since pack doesn't allow overlap of widgets.
        self.menu2.pack(side="left")
        # Now we can generate our label that should change according to our
        # options. At the start of our GUI we set the displayed text to the
        # contents of var1 and the background color (bg) to the contents of var2
        self.label1 = tk.Label(self.root, text=self.var1.get(), bg=self.var2.get())
        # We just pack our label on the right side of our GUI.
        self.label1.pack(side="right")
        # Now we start the mainloop to initate our GUI
        self.root.mainloop()

    # Now we can define our functions to be able to change our label according
    # to the made choices. Since these functions are associated with menus we
    # have to hand over two arguments. First the GUI itself and second the
    # choice of the respective menu. Keep in mind that if you don't hand over
    # two arguments you run into errors.
    def display_selected(self, choice):
        # First we have to read in the current value of our var1 that is
        # associated with our menu. This can be simply done by using get()
        choice = self.var1.get()
        # For this example I print out the choice in the terminal but normally
        # this isn't necessary
        print(choice)
        # Now I can change the text in my label by simply handing over the
        # chosen option to a config method of our label.
        self.label1.config(text=choice)

    # I included a second function for changing the background color of our
    # label. I wrote the function in a compacter way than the first one to show
    # you how you can safe some lines in your source code. As you can see you
    # can use the config method in the same way we used it for the creation of
    # the label.
    def change_bg(self, choice):
        # This simpel line changes the background color of our label according
        # to the value chosen by the user.
        self.label1.config(bg=self.var2.get())


# Last but not least we have to start our GUI
Options()
