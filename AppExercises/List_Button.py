import tkinter as tk


class ListBox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.root.title("Listbox with multiple foods")
        self.Foods = [
            "Sushi",
            "Burger",
            "Pasta",
            "Soup",
            "Cornflakes",
            "Steak",
            "Salat",
            "Döner",
            "Cake",
        ]
        self.FoodChoice = tk.StringVar(value=self.Foods)
        self.listbox = tk.Listbox(
            self.root,
            listvariable=self.FoodChoice,
            height=6,
            selectmode="multiple",
            selectbackground="blue",
            selectforeground="snow",
        )
        self.button1 = tk.Button(
            self.root, text="Order now", command=self.FoodSelection
        )
        self.listbox.pack(fill="both")
        self.button1.pack()

        self.FoodOrder = tk.Message(self.root, text="Nothing ordered yet", width=150)
        self.FoodOrder.pack()

        self.root.mainloop()

    def FoodSelection(self):
        foods = []
        foodIndex = self.listbox.curselection()
        for i in foodIndex:
            index = self.listbox.get(i)
            foods.append(index)
        # for meal in foods:
        #     print("You selected:", meal)
        self.FoodOrder.config(text=foods)


ListBox()
