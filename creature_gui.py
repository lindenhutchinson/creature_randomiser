from tkinter import *
from tkinter import ttk
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

        self.saved_creatures = {}
        self.save_creatures = BooleanVar(value=0)
        self.saved_creature_string = ''
        self.creature_choice = StringVar()
        
        # label for holding the creature image
        self.creature_label = Label(self.main)

        # button for toggling whether the next list of random creatures should be saved
        self.save_creatures_button = Checkbutton(self.main, text="Save next creature list", variable=self.save_creatures)

        # button for retrieving the previously saved creature list
        self.get_saved_creatures_button = Button(self.main, text="Get saved creatures", command=self.get_saved_creatures)

        # button for generating new random creatures
        self.get_random_button = Button(self.main, text="Randomize", command=self.get_random_creatures, width=43)

        # label for providing information on either the saved creatures or the number of possible creatures
        self.info_label = Label(self.main, textvariable=self.creature_info, font=(FONT, 12))
        
        # input for the number of random creatures to be generated
        self.num_input = ttk.Combobox(self.main, textvariable=self.num_choice, width=20, values=[i for i in range(1, 9)])
        num_label = Label(self.main, text = "The number of creatures :",font = (FONT, 10))

        # input for the cr of the random creatures to be generated
        self.cr_input = ttk.Combobox(self.main, textvariable=self.cr_choice, width=20, values=self.master.get_all_cr())
        self.cr_input.current(0)
        cr_label = Label(self.main, text = "The CR :",font = (FONT, 10))

        # input for the type of the random creatures to be generated
        self.type_input = ttk.Combobox(self.main, textvariable=self.type_choice, width=20, values=self.master.get_all_type(), )
        self.type_input.current(0)
        type_label = Label(self.main, text = "The Type :",font = (FONT, 10))

        # placing the creature image, and the buttons related to saving creatures
        self.creature_label.place(x=350, y=60)
        self.save_creatures_button.place(x=350, y=20)
        self.get_saved_creatures_button.place(x=500, y=20)

        # placing the input buttons and their labels
        self.get_random_button.place(x=25, y=20)
        self.num_input.place(x=190, y=50)
        num_label.place(x=25, y=50)
        self.cr_input.place(x=190, y=75)
        cr_label.place(x=25, y=75)
        self.type_input.place(x=190, y=100)
        type_label.place(x=25, y=100)
        self.info_label.place(x=25, y=125)

    # retrieves an image named after a creature
    def get_creature_image(self, creature_name):
        img = f"{self.image_dir}/{creature_name}.png"
        self.image = PhotoImage(file=img)
        self.creature_label.configure(image=self.image)
        self.creature_label.image=self.image
    
    # unplace all creature buttons and recreate the button list
    def forget_creature_buttons(self):
        for btn in self.creature_buttons:
            btn.place_forget()

        self.creature_buttons = []
    
    # retrieve the saved creature list and place it onto the page
    def get_saved_creatures(self):
        if self.saved_creatures:
            self.forget_creature_buttons()
            x=20
            y=150
            for name, num in self.saved_creatures.items():
                btn = Button(self.main, text=f"{num} x {name}", width=43, command=partial(self.get_creature_image, name))
                btn.place(x=x, y=y)
                y+=40
                self.creature_buttons.append(btn)
        
            self.creature_info.set(f"Retrieved {self.saved_creature_string}")
        else:
            self.creature_info.set("No saved creatures found")

    # generate and place a new list of creatures
    def get_random_creatures(self):
        num = self.num_choice.get()
        cr = self.cr_choice.get()
        ctype = self.type_choice.get()

        self.forget_creature_buttons()
            
        random_creatures = self.master.get_random_creatures(num,cr,ctype)
        save_creatures = self.save_creatures.get()
    
        if random_creatures:
            x=20
            y=150
            total = 0
            for name, num in random_creatures.items():
                total+=num
                btn = Button(self.main, text=f"{num} x {name}", width=43, command=partial(self.get_creature_image, name))
                btn.place(x=x, y=y)
                y+=40
                self.creature_buttons.append(btn)

            if save_creatures:
                self.saved_creatures = random_creatures
                self.saved_creature_string=f"{total} CR {cr} {ctype}{'s' if total > 1 and ctype!='Fey' else ''}"
                self.creature_info.set(f"Saved {self.saved_creature_string}")
                self.save_creatures_button.invoke()

        if not save_creatures:     
            self.creature_info.set(self.master.get_possible_creatures_string(cr, ctype))
