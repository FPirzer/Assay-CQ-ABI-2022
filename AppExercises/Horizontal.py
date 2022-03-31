import tkinter as tk


class Horizontal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.v1 = tk.DoubleVar()
        self.scale1 = tk.Scale(
            self.root, variable=self.v1, from_=1, to=100, orient="horizontal"
        )
        self.label1 = tk.Label(self.root, text="Horizontal Scaler")
        self.button1 = tk.Button(
            self.root, text="Display Horizontal", command=self.show1, bg="yellow"
        )
        self.label2 = tk.Label(self.root)
        self.scale1.pack(anchor="center")
        self.label1.pack()
        self.button1.pack(anchor="center")
        self.label2.pack()
        self.root.mainloop()

    def show1(self):
        sel = "Horizontal Scale Value = " + str(self.v1.get())
        self.label2.config(text=sel,)


Horizontal()
