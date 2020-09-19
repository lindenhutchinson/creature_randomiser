from master import Master
from creature_utils import *
from tkinter import *
from creature_gui import CreatureGui
import os 


if __name__ == "__main__":
    # for scraping the data required for the gui
    # create_creatures_csv('path_to_csv')
    # take_creature_screenshots('images', './data/creatures.csv')


    # for running the gui
    master = Master(get_creatures_from_csv('./data/creatures.csv'))
    main = Tk()
    main.geometry("1500x1000")
    c = CreatureGui(main, master, 'images')
    main.mainloop()
