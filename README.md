# Creature Randomizer

This program has two parts

First you will need to scrap some data on creatures. There are two functions for retrieving creature data:

* create_creatures_csv('./data/creatures.csv')
* take_creature_screenshots('image_dir', './data/creatures.csv')

These use the scraper class and will require a chromedriver to be installed, either in the directory or on your PATH.

When you have a creatures.csv and a directory full of images, you are ready to start the gui:

    master = Master(get_creatures_from_csv('./data/creatures.csv'))
    main = Tk()
    main.geometry("1500x1000")
    c = CreatureGui(main, master, 'image_dir')
    main.mainloop()

