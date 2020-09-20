# DnD Creature Randomizer

This program can be used to generate a random list of 5e creatures according to type and CR. You can adjust how many random creatures should be generated. I created it so I would have an easier time as a 5e Druid who uses conjuration spells.

All the data for the program to run is provided in the repo (./data and ./images) so you should be fine to run the main.py file to start the program.

Although data is already provided, if you like you can scrape the data again/configure the script a little to scrape from another source. The two functions involved in this process are located in creature_utils.py and are called:

* create_creatures_csv('/path/to/csv_file')
* take_creature_screenshots('directory/to/save/images', '/path/to/csv_file')

These functions use the Scraper class from scraper.py, which will require a Selenium chromedriver in the root directory.
