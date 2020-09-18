from tkinter import *
from tkinter import ttk
from master import Master
FONT = "Helvetica"

class CreatureGui:
    def __init__(self, main, master):
        self.main  = main
        self.master = master
        self.creature_info = StringVar()
        self.creature_text = StringVar()
        self.num_choice = IntVar(value=1)
        self.cr_choice = StringVar()
        self.type_choice = StringVar()


        self.get_random_button = Button(self.main, text="Randomize", command=self.get_random_creatures, width=20)
        self.info_label = Label(self.main, textvariable=self.creature_info, font=(FONT, 12))
        self.creatures_label = Label(self.main, textvariable=self.creature_text, font=(FONT, 12))
        

        self.num_input = ttk.Spinbox(self.main, textvariable=self.num_choice)
        self.cr_input = ttk.Combobox(self.main, textvariable=self.cr_choice, width=20, values=self.master.get_all_cr())
        self.type_input = ttk.Combobox(self.main, textvariable=self.type_choice, width=20, values=self.master.get_all_type())
        self.cr_input.current(0)
        self.type_input.current(0)

        self.creatures_label.place(x=200, y=60)
        self.info_label.place(x=200, y=10)
        self.num_input.place(x=10, y=25)

        self.get_random_button.place(x=10, y=50)
        self.cr_input.place(x=10, y=90)
        self.type_input.place(x=10, y=110)

        
    def get_random_creatures(self):
        num = self.num_choice.get()
        cr = self.cr_choice.get()
        ctype = self.type_choice.get()

        random_text = self.master.get_random_creatures_string(num,cr,ctype)
        self.creature_text.set(random_text)
        self.creature_info.set(self.master.get_possible_creatures_string(cr, ctype))





