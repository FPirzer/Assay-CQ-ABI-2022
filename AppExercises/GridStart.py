import tkinter as tk


class Grid:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("240x90")
        self.root.title("Login")
        self.root.resizable(0, 0)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        self.login_button = tk.Button(self.root, text="Login")
        self.login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        self.root.mainloop()


Grid()
