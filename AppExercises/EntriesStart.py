"""
This is the script that generates the second GUI we used during our Course on
the 25.2022. Each GUI we create will be a different script, so that it's
easier to run them and see what they're doing. This GUI takes the values of two
entries and adds them up. The result is than displayed in a label.
"""
# First we have to import tkinter to be able to create our GUIs.
import tkinter as tk

# First we define our GUI as a new class as we saw in Hello1.py
class Adder:
    # We create our constructor so that we can initiate our GUI.
    def __init__(self):
        # Again the first thing we have to do is creating our root, so that we
        # can than put everything in it later on.
        self.root = tk.Tk()
        # To be able to work with the contents of our entries we have to define
        # inputs in the form of VarVars. There are only three types of VarVars
        # StringVar for strings, IntVar for integer and BooleanVar for True or
        # False. Since we want to be able to work with floats alter on we have
        # to use StringVars in this case and cast them to flaots later on.
        self.input1 = tk.StringVar()
        self.input2 = tk.StringVar()
        # Now we set up our two entries. The parameters for both are nearly
        # identical, since we want them to look the same. The only difference is
        # which input is associated with which entry.
        self.edit1 = tk.Entry(
            self.root,  # This is the parent of our entry field
            textvariable=self.input1,  # This tells tkinter that the input1 gets
            # its value from the textinput that is in this entry. This is
            # important later on, than we run our getter() method for the inputs
            # in our function to add up the values.
            font=15,  # This is the font size
            width=33,  # This is the width of our entry
            bg="light slate gray",  # This is the color of our entry
            fg="snow",  # This is the color of the text in our entry
        )
        self.edit2 = tk.Entry(
            self.root,
            textvariable=self.input2,  # Here we can see that the second entry is
            # combined with the second input. So now each input has its own
            # entry field it's associated with.
            font=15,
            width=33,
            bg="light slate gray",
            fg="snow",
        )
        # Now we pack our two entries at the top of our GUI. They are directly
        # under each other.
        self.edit1.pack()
        self.edit2.pack()
        # Next we have to set up our Button, so that we can start the addition
        # of the two inputs. The main setup is similiar to the one we saw in
        # Hello1.py
        self.button1 = tk.Button(
            self.root,
            text="Click Me",
            command=self.add_up,  # This time we associate the function
            # add_up with the button, so that we can it later with a single
            # click. The function is defined further down below. Since we don't
            # want ot hand over anything to our funtion we can use the command
            # attribute without lambda, but keep in mind to call the function
            # without brackets. Otherwise the function would be executed on the
            # Construction of our GUI
            width=30,
            font=15,
            fg="yellow",
            bg="black",
            activebackground="grey",
            activeforeground="snow",
        )
        # Again we pack our Button in our GUI and its located directly under our
        # two entries.
        self.button1.pack()
        # Last but not least we create a label so that we can display the result
        # In our GUI.
        self.w = tk.Label(
            self.root,  # This is the parent of our Widget, in this case root
            text="",  # This is the text that is displayed in our Label
            font=15,  # This is the font size of our Label
            width=33,  # This is the width of our Label, depending on the size
            # of our text
            fg="blue",  # This is the color of the text
            bg="grey",  # This is the color of the background
        )
        # We use pack to out our label in our GUI. It's now located at the
        # bottom of our GUI.
        self.w.pack()
        # Last but not least we start the mainloop() so that our GUI can be
        # created.
        self.root.mainloop()

    # Now we define our function add_up so that we can use it with our button.
    # Since this function works without any additional parameters we just need
    # self in the brackets of our signature.
    def add_up(self):
        # First we have to read out the values that are in our two entries. This
        # is only possible witht he help of the get() method. In the examples
        # below we read in the string that is in our entries and assign the
        # value first to our inputs. This value is than assigned to our two
        # variables Nr1 and Nr2.
        Nr1 = self.input1.get()
        Nr2 = self.input2.get()
        # Now that we have our two inputs in our variables Nr1 and Nr2 we can
        # work with them. In our case we just want to add them together. To do
        # this we cast them to floats and add them up. Keep in mind that this
        # returns an error, if the values inside our entries are strings.
        ergebnis = float(Nr1) + float(Nr2)
        # Now we can put the result in our Label. Therefore we have to change
        # the attribute text of our label. This can be done by using the config
        # method, as we also saw in Hello1.py.
        self.w.config(text=str(ergebnis))


# To start our GUI we simply call back our class without any arguments
Adder()
