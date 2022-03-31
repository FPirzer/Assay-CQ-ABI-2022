import tkinter as tk


class Message:
    def __init__(self):
        self.root = tk.Tk()
        self.whatever = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
        self.msg = tk.Message(
            self.root, text=self.whatever, bg="lightgreen", font=("times", 24, "italic")
        )
        self.msg2 = tk.Label(
            self.root, text="I am a test", bg="blue", font=("Times", 24, "bold")
        )
        self.msg2.pack()
        self.msg.pack()
        self.root.mainloop()


Message()
