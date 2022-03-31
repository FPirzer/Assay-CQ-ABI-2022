import tkinter as tk


class CheckBox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Check Box App")
        self.root.geometry("600x200")
        self.BoxValue1 = tk.BooleanVar()
        self.BoxValue1.set(False)
        self.BoxValue2 = tk.BooleanVar()
        self.BoxValue2.set(False)
        self.BoxValue3 = tk.BooleanVar()
        self.BoxValue3.set(False)
        self.BoxValue4 = tk.BooleanVar()
        self.BoxValue4.set(False)
        self.BoxValue5 = tk.BooleanVar()
        self.BoxValue5.set(False)

        self.checkbox1 = tk.Checkbutton(self.root, text="Check 1", var=self.BoxValue1)
        self.checkbox1.pack()

        self.checkbox2 = tk.Checkbutton(self.root, text="Check 2", var=self.BoxValue2)
        self.checkbox2.pack()

        self.checkbox3 = tk.Checkbutton(self.root, text="Check 3", var=self.BoxValue3)
        self.checkbox3.pack()

        self.checkbox4 = tk.Checkbutton(self.root, text="Check 4", var=self.BoxValue4)
        self.checkbox4.pack()

        self.checkbox5 = tk.Checkbutton(self.root, text="Check 5", var=self.BoxValue5)
        self.checkbox5.pack()

        self.CheckButton = tk.Button(
            self.root, text="Check your input", width=80, command=self.CheckSummary,
        )
        self.CheckButton.pack()

        self.CheckLabel = tk.Label(self.root, text="Nothing checked yet")
        self.CheckLabel.pack()

        self.root.mainloop()

    def CheckSummary(self):
        Checking1 = self.BoxValue1.get()
        Checking2 = self.BoxValue2.get()
        Checking3 = self.BoxValue3.get()
        Checking4 = self.BoxValue4.get()
        Checking5 = self.BoxValue5.get()
        if Checking1:
            Checking1 = "checked"
        else:
            Checking1 = "not checked"
        if Checking2:
            Checking2 = "checked"
        else:
            Checking2 = "not checked"
        if Checking3:
            Checking3 = "checked"
        else:
            Checking3 = "not checked"
        if Checking4:
            Checking4 = "checked"
        else:
            Checking4 = "not checked"
        if Checking5:
            Checking5 = "checked"
        else:
            Checking5 = "not checked"

        self.CheckLabel.config(
            text=f"Check Box 1 is {Checking1}\nCheck Box 2 is {Checking2}\nCheck Box 3 is {Checking3}\nCheck Box 4 is {Checking4}\nCheck Box 5 is {Checking5}\n"
        )


CheckBox()
