from tkinter import *
from tkinter import ttk
from master import Master
from functools import partial

FONT = "Helvetica"

class CreatureGui:
    def __init__(self, main, master, image_dir):
        self.main = main
        self.master = master
        self.image_dir = image_dir
        self.creature_info = StringVar()
        self.num_choice = IntVar(value=1)
        self.cr_choice = StringVar()
        self.type_choice = StringVar()
        self.creature_buttons = []
        self.creature_choice =StringVar()

        self.creature_label = Label(self.main)

        self.num_input = ttk.Spinbox(self.main, textvariable=self.num_choice, from_=0, to=8, width=20)

        self.get_random_button = Button(self.main, text="Randomize", command=self.get_random_creatures, width=43)
        self.info_label = Label(self.main, textvariable=self.creature_info, font=(FONT, 12))
        
        self.num_input = ttk.Combobox(self.main, textvariable=self.num_choice, width=20, values=[i for i in range(1, 9)])
        self.cr_input = ttk.Combobox(self.main, textvariable=self.cr_choice, width=20, values=self.master.get_all_cr())
        self.type_input = ttk.Combobox(self.main, textvariable=self.type_choice, width=20, values=self.master.get_all_type())
        self.cr_input.current(0)
        self.type_input.current(0)

        self.creature_label.place(x=375, y=60)
        self.info_label.place(x=375, y=20)


        num_label = Label(self.main, text = "The number of creatures :",font = (FONT, 10))
        cr_label = Label(self.main, text = "The CR :",font = (FONT, 10))
        type_label = Label(self.main, text = "The Type :",font = (FONT, 10))

        self.get_random_button.place(x=25, y=20)

        self.num_input.place(x=190, y=50)
        num_label.place(x=25, y=50)

        self.cr_input.place(x=190, y=75)
        cr_label.place(x=25, y=75)

        self.type_input.place(x=190, y=100)
        type_label.place(x=25, y=100)

    def get_creature_image(self, creature_name):
        img = f"{self.image_dir}/{creature_name}.png"
        self.image = PhotoImage(file=img)
        self.creature_label.configure(image=self.image)
        self.creature_label.image=self.image
    
    def forget_creature_buttons(self):
        for btn in self.creature_buttons:
            btn.place_forget()

        self.creature_buttons = []
        
    def get_random_creatures(self):
        num = self.num_choice.get()
        cr = self.cr_choice.get()
        ctype = self.type_choice.get()

        if len(self.creature_buttons) > 0:
            self.forget_creature_buttons()
        random_creatures = self.master.get_random_creatures(num,cr,ctype)
    
        if random_creatures:
            x=20
            y=150
            
            for name, num in random_creatures.items():
                btn = Button(self.main, text=f"{num} x {name}", width=43, command=partial(self.get_creature_image, name))
                btn.place(x=x, y=y)
                y+=40
                self.creature_buttons.append(btn)

        self.creature_info.set(self.master.get_possible_creatures_string(cr, ctype))
