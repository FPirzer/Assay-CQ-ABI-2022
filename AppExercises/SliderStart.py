import tkinter as tk


class CoordSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.Yvalue = tk.DoubleVar()
        self.Xvalue = tk.DoubleVar()

        self.YAxis = tk.Scale(
            self.root, variable=self.Yvalue, from_=100, to=1, orient="vertical"
        )
        self.YAxis.pack(anchor="center")

        self.YAxisLabel = tk.Label(self.root, text="Vertical Slider")
        self.YAxisLabel.pack()

        self.XAxis = tk.Scale(
            self.root, variable=self.Xvalue, from_=1, to=100, orient="horizontal"
        )
        self.XAxis.pack()

        self.XAxisLabel = tk.Label(self.root, text="Horizontal Slider")
        self.XAxisLabel.pack()

        self.CoordButton = tk.Button(
            self.root, text="Display Coordinates", command=self.CoordCalc
        )
        self.CoordButton.pack(anchor="center")

        self.CoordLabel = tk.Label(self.root, text="No coordiantes yet")
        self.CoordLabel.pack()

        self.root.mainloop()

    def CoordCalc(self):
        YX = f"Coordinates are Y{self.Yvalue.get()} and X{self.Xvalue.get()}"
        self.CoordLabel.config(text=YX)


CoordSystem()
