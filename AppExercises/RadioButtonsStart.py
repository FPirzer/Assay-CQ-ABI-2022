import tkinter as tk


class RadioButtons:
    def __init__(self):
        self.root = tk.Tk()
        self.Food = tk.StringVar()
        self.Food.set(0)
        self.Takeout = tk.StringVar()
        self.Takeout.set(0)
        self.label1 = tk.Label(self.root, text="Pick one")
        self.label1.pack()

        self.RadioButtonRound1 = tk.Radiobutton(
            self.root,
            text="Sushi",
            variable=self.Food,
            value="Sushi",
            # you can also add a function for every time the option is clicked
            # command=self.ShowChoice,
            width=20,
        )
        self.RadioButtonRound1.pack(anchor="w")

        self.RadioButtonRound2 = tk.Radiobutton(
            self.root, text="Burger", variable=self.Food, value="Burger", width=20,
        )
        self.RadioButtonRound2.pack(anchor="w")

        self.RadioButtonRound3 = tk.Radiobutton(
            self.root, text="Pasta", variable=self.Food, value="Pasta", width=20,
        )

        self.RadioButtonRound3.pack(anchor="w")

        self.RadioButtonSquare1 = tk.Radiobutton(
            self.root,
            text="Table order",
            variable=self.Takeout,
            value="Table order",
            indicator=0,
            width=20,
        )
        self.RadioButtonSquare1.pack(anchor="w")

        self.RadioButtonSquare2 = tk.Radiobutton(
            self.root,
            text="To go",
            variable=self.Takeout,
            value="To go",
            indicator=0,
            width=20,
        )
        self.RadioButtonSquare2.pack(anchor="w")

        self.RadioButtonSquare3 = tk.Radiobutton(
            self.root,
            text="Cooking box",
            variable=self.Takeout,
            value="Cooking box",
            indicator=0,
            width=20,
        )
        self.RadioButtonSquare3.pack(anchor="w")

        self.CheckButton = tk.Button(
            self.root, text="Check your input", width=80, command=self.CheckOut
        )
        self.CheckButton.pack()

        self.root.mainloop()

    def CheckOut(self):

        print(
            f"Your order for {self.Food.get()} as a {self.Takeout.get()} will be placed"
        )


RadioButtons()
