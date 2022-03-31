import tkinter as tk


class TextApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text App with features")
        self.Textfield1 = tk.Text()
        self.Textfield1.pack()
        # Spacing 1 makes space over the characters, spacing1=20
        # Spaceing2 makes space after you go over the line
        # self.Textfield2 = tk.Text(spacing2=20)
        # self.Textfield2.pack()
        # Spacing 3 makes Space after the characters
        # self.Textfield3 = tk.Text(spacing3=20)
        # self.Textfield3.pack()

        self.CharacterCounter = tk.Label(self.root, text="This is the counter label")
        self.CharacterCounter.pack()

        self.LastOptionPressed = tk.Label(
            self.root, text="You didn't press any buttons yet."
        )
        self.LastOptionPressed.pack()

        self.InsertStartButton = tk.Button(
            self.root, text="Insert a start phrase", command=lambda: InsertStart(self)
        )
        self.InsertStartButton.pack()

        self.InsertEndButton = tk.Button(
            self.root, text="Insert an ending phrase", command=lambda: InsertEnd(self)
        )
        self.InsertEndButton.pack()

        self.CountButton = tk.Button(
            self.root, text="Count the characters", command=lambda: Count(self)
        )
        self.CountButton.pack()

        self.ClearButton = tk.Button(
            self.root, text="Clear all text", command=lambda: ClearAll(self)
        )
        self.ClearButton.pack()

        self.PrintButton = tk.Button(
            self.root, text="Print text to consol", command=lambda: PrintAll(self)
        )
        self.PrintButton.pack()

        self.root.mainloop()


def Count(self):
    self.Counter = len(self.Textfield1.get(1.0, "end-1c"))
    self.CharacterCounter.config(text=self.Counter)
    self.LastOptionPressed.config(text="You counted the characters")


def InsertStart(self):

    self.Textfield1.insert(1.0, "Once upon a time...\n")
    self.LastOptionPressed.config(text="You insert something at the start")


def InsertEnd(self):
    self.Textfield1.insert("end", "\nAnd thats how the story ends.")
    self.LastOptionPressed.config(text="You insert something at the end")


def ClearAll(self):
    self.Textfield1.delete(1.0, "end")
    self.LastOptionPressed.config(text="You deleted everything")


def PrintAll(self):
    print(self.Textfield1.get(1.0, "end"))
    self.LastOptionPressed.config(text="You printed everything to the console.")


TextApp()
