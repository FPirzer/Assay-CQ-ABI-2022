import tkinter as tk


class pack_folien_layout:
    def __init__(self):
        self.root = tk.Tk()

        # erstellung der widgets -
        ####################### Ebene 1 #####################

        self.gelb_oben = tk.Frame(self.root)
        self.gruen = tk.Frame(self.root)
        self.gelb_unten = tk.Frame(self.root)

        ####################### Ebene 2 #####################

        self.label8 = tk.Label(self.gelb_oben, text="Label 8")
        self.rot = tk.Frame(self.gruen)
        self.braun = tk.Frame(self.gruen)
        self.label9 = tk.Label(self.gelb_unten, text="Label 9")

        ####################### Ebene 3 #####################

        self.button0 = tk.Button(self.rot, text="Button 0")
        self.button1 = tk.Button(self.rot, text="Button 1")
        self.button2 = tk.Button(self.rot, text="Button 2")
        self.button3 = tk.Button(self.rot, text="Button 3")
        self.button4 = tk.Button(self.rot, text="Button 4")

        self.button5 = tk.Button(self.braun, text="Button 5")
        self.button6 = tk.Button(self.braun, text="Button 6")
        self.button7 = tk.Button(self.braun, text="Button 7")

        ###################### Packen der Widgets ###########
        ###################### Ebene 1 ######################

        self.gelb_oben.pack()  # defaultwert: top
        self.gruen.pack()
        self.gelb_unten.pack()

        ####################### Ebene 2 #####################

        self.label8.pack()

        self.rot.pack(side="left")
        self.braun.pack(side="left")  # ,anchor="n"

        self.label9.pack()

        ####################### Ebene 3 #####################

        self.button0.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()

        self.button5.pack()
        self.button6.pack()
        self.button7.pack()

        self.root.mainloop()


if __name__ == "__main__":
    pack_folien_layout()
