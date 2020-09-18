
from master import Master
from creature_utils import create_creatures_csv
from tkinter import *
from creature_gui import CreatureGui



if __name__ == "__main__":
    master = Master()
    master.get_creatures_from_csv('./data/creatures.csv')
    main = Tk()
    main.geometry("1000x600")
    
    c = CreatureGui(main, master)
    main.mainloop()
