import tkinter as tk


class Options:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x200")
        self.FGSelect = tk.StringVar()
        self.BGSelect = tk.StringVar()
        self.CountrySelect = tk.StringVar()
        self.FGSelect.set("Choose something")
        self.BGSelect.set("Choose something")
        self.CountrySelect.set("Choose something")
        self.ForegroundMenu = tk.OptionMenu(
            self.root,
            self.FGSelect,
            "Red",
            "Blue",
            "Green",
            command=self.ChangeDisplay1,
        )
        self.ForegroundMenu.pack()

        self.BackgroundMenu = tk.OptionMenu(
            self.root,
            self.BGSelect,
            "Red",
            "Blue",
            "Green",
            command=self.ChangeDisplay2,
        )
        self.BackgroundMenu.pack()

        self.CountryMenu = tk.OptionMenu(
            self.root,
            self.CountrySelect,
            "Germany",
            "Britain",
            "Spain",
            "Japan",
            "France",
            "USA",
            "Italy",
            command=self.ChangeDisplay3,
        )
        self.CountryMenu.pack()

        self.label1 = tk.Label(self.root, text="Choose a country")
        self.label1.pack()
        self.root.mainloop()

    def ChangeDisplay1(self, choice):
        choice1 = self.FGSelect.get()
        self.label1.config(fg=choice1)

    def ChangeDisplay2(self, choice):
        choice2 = self.BGSelect.get()
        self.label1.config(bg=choice2)

    def ChangeDisplay3(self, choice):
        choice3 = self.CountrySelect.get()
        self.label1.config(text=choice3)


# print(
#     f"Your foreground is {choice1}, your background is {choice2} and the country is {choice3}"
# )

Options()
