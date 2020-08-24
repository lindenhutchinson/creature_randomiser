import csv
import random
from creatures import Creature, CreatureParser, Master
from scraper import Scraper
from gui import Gui
def get_creatures_from_csv(dir):
    data = []
    with open(dir, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(Creature(row[0].strip(), row[1].strip(), row[2].strip()))

    return data

def create_creatures_csv(dir):
    s = Scraper('https://dnd-wiki.org/wiki/5e_Beast_List', './chromedriver')
    s.click_on_xpath('/html/body/div[4]/div[2]/div[4]/div/table/thead/tr/th[6]')
    table = s.get_text_by_class('sortable')
    s.quit()
    parser = CreatureParser(table)
    master = Master(parser.get_creatures())
    master.write_to_file(dir)

# create_creatures_csv('creatures.csv')

# creatures = get_creatures_from_csv('creatures.csv')
# master = Master(creatures)
# crs = ['0', '1/8', '1/4','1/2', '1', '2','3','4','5','6','7']
# master.get_random_creatures(8, '1/4')


creatures = get_creatures_from_csv('creatures.csv')
master = Master(creatures)
g = Gui(master)
g.main()