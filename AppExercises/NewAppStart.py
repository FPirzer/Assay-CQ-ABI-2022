import tkinter as tk


class NewApp:
    def __init__(self, arg_Text):
        self.root = tk.Tk()
        self.root.title("AwesomeApp3000")
        #
        # self.w = tk.Label(
        #     self.root, text=arg_Text, height=20, width=20, bg="gray", fg="black"
        # )
        # self.w.pack()
        #
        # self.Box2 = tk.Label(
        #     self.root,
        #     text="Hi I am Box 2",
        #     height=10,
        #     width=15,
        #     bg="green",
        #     fg="light salmon",
        # )
        # self.Box2.pack(side="right")
        #
        # self.Box3 = tk.Label(
        #     self.root,
        #     text="Hi I am Box 3",
        #     height=15,
        #     width=20,
        #     bg="MediumPurple1",
        #     fg="thistle3",
        # )
        # self.Box3.pack()
        self.NrClick = 0
        self.ButCount = tk.Label(self.root, text="You didn't click yet!")
        self.ButCount.pack()
        self.ClickerButton = tk.Button(
            self.root, text="Rise the number by one", command=lambda: plusOne(self)
        )
        self.ClickerButton.pack()

        def plusOne(self):
            self.NrClick += 1
            self.ButCount.config(text=self.NrClick)

        # self.Button1 = tk.Button(
        #     self.root,
        #     text="Add up",
        #     command=lambda: adding(self),
        #     height=10,
        #     width=20,
        #     fg="yellow",
        #     bg="black",
        #     activeforeground="black",
        #     activebackground="gray",
        # )
        # self.Button1.pack()
        # self.input1 = tk.StringVar()
        # self.input2 = tk.StringVar()
        # self.edit1 = tk.Entry(self.root, textvariable=self.input1)
        # self.edit2 = tk.Entry(self.root, textvariable=self.input2)
        # self.edit1.pack()
        # self.edit2.pack()
        self.root.mainloop()


# def adding(self):
#     number1 = self.input1.get()
#     number2 = self.input2.get()
#     sum = float(number1) + float(number2)
#     print(sum)
#     self.w.config(text=str(sum))


NewApp("What a mess")
