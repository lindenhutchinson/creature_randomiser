import csv
import random
from creatures import Creature, CreatureParser, Master
from scraper import Scraper
from gui import Gui


def get_creatures_from_csv(dir):
    c_list = []
    with open(dir, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            c_list.append(Creature(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()))

    return c_list

def create_creatures_csv(dir):

    s = Scraper('https://www.jsigvard.com/dnd/Monsters.html', './chromedriver')
    s.click_on_xpath('/html/body/div[1]/div/div[2]/div/table/thead/tr/th[5]')
    table = s.get_text_by_class('table')
    s.quit()
    parser = CreatureParser(table) 
    master = Master(parser.get_creatures())
    master.write_to_file(dir)


creatures = get_creatures_from_csv('creatures.csv')
master = Master(creatures)
g = Gui(master)
g.main()
