from creature_master import Master
from creature_utils import create_creatures_csv,take_creature_screenshots,get_creatures_from_csv
from tkinter import *
from creature_gui import CreatureGui

def run_gui():
    master = Master(get_creatures_from_csv('./data/creatures.csv'))
    main = Tk()
    main.geometry("1500x1000")
    c = CreatureGui(main, master, 'images')
    main.mainloop()

# requires chromedriver.exe in the same directory
def scrape_data(csv_path, image_directory):
    create_creatures_csv(csv_path)
    take_creature_screenshots(image_directory, csv_path)




if __name__ == "__main__":
    run_gui()
