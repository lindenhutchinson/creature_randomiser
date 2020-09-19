
from master import Master
from creature_utils import create_creatures_csv, take_creature_screenshots
from tkinter import *
from creature_gui import CreatureGui



if __name__ == "__main__":
    # create_creatures_csv('path_to_csv')
    # take_creature_screenshots('image_directory')

    master = Master()
    master.get_creatures_from_csv('./data/creatures.csv')
    main = Tk()
    main.geometry("1500x1000")
    
    c = CreatureGui(main, master, 'new_images')
    main.mainloop()
