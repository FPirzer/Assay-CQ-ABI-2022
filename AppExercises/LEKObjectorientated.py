import tkinter as tk


class LEK_Objects:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.ConversionChoice = tk.StringVar()
        self.ConversionChoice.set("Choose your conversion")
        self.TempChoices = tk.OptionMenu(
            self.root,
            self.ConversionChoice,
            "Celcius to Fahrenheit",
            "Fahrenheit to Celcius",
            "Celcius to Kelvin",
            "Kelvin to Celcius",
            "Fahrenheit to Kelvin",
            "Kelvin to Fahrenheit",
        )
        self.TempChoices.pack()

        self.TempInputField = tk.DoubleVar()
        self.TempInputField = ""
        self.TempInput = tk.Entry(self.root, textvariable=self.TempInputField)
        self.TempInput.pack()

        self.ConversionButton = tk.Button(
            self.root, text="Convert my Temperature", command=lambda: TempCalc(self)
        )
        self.ConversionButton.pack()

        self.TempLabel = tk.Label(self.root, text="Nothing converted yet")
        self.TempLabel.pack()

        self.root.mainloop()


# Celsius = 5/9 * (Fahrenheit - 32).
# Celsius = Kelvin - 273.15.


def TempCalc(self):

    if self.ConversionChoice.get() == "Celcius to Fahrenheit":
        C = float(self.TempInput.get())
        F = C * 9 / 5 + 32
        self.TempLabel.config(text=f"{F}° Fahrenheit")

    elif self.ConversionChoice.get() == "Fahrenheit to Celcius":
        F = float(self.TempInput.get())
        C = (F - 32) * 5 / 9
        self.TempLabel.config(text=f"{C}° Celcius")

    elif self.ConversionChoice.get() == "Celcius to Kelvin":
        C = float(self.TempInput.get())
        K = C + 273.15
        self.TempLabel.config(text=f"{K} Kelvin")

    elif self.ConversionChoice.get() == "Kelvin to Celcius":
        K = float(self.TempInput.get())
        C = K - 273.15
        self.TempLabel.config(text=f"{C}° Celcius")

    elif self.ConversionChoice.get() == "Fahrenheit to Kelvin":
        F = float(self.TempInput.get())
        K = (F - 32) * 5 / 9 + 273.15
        self.TempLabel.config(text=f"{K} Kelvin")

    elif self.ConversionChoice.get() == "Kelvin to Fahrenheit":
        K = float(self.TempInput.get())
        F = (K - 273.15) * 9 / 5 + 32
        self.TempLabel.config(text=f"{F}° Fahrenheit")

    else:
        self.TempLabel.config(text="No conversion choosen")


LEK_Objects()
