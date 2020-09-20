from bs4 import BeautifulSoup
from scraper import Scraper
from creature_master import Master, Creature
import csv

def get_creatures_from_csv(dir):
    creatures =[]
    with open(dir, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            creatures.append(Creature(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()))

    return creatures

def write_to_file(dir, creatures):
    with open(dir, 'w', encoding="utf-8") as fn:
        for creature in creatures:
            fn.write(creature.to_string()+'\n')

def get_creatures(soup):
    rows = soup.find_all('tr')
    creatures = []
    for row in rows[2:]:
        data = row.find_all('td')
        ctype = data[2].get_text()
        # Currently only want to deal with three types of creatures, 
        # but it is possible to comment out this line and retrieve creatures of all types
        if ctype in ['Beast', 'Fey', 'Elemental']:
            name = data[0].get_text()
            href = 'https://www.jsigvard.com/dnd/'+data[0].find('a').get('href')
            cr = str(data[4].contents[1])
            creatures.append(Creature(name, cr, href, ctype))

    return creatures

def create_creatures_csv(dir):
    s = Scraper('https://www.jsigvard.com/dnd/Monsters.html', './chromedriver')
    s.click_on_xpath('/html/body/div[1]/div/div[2]/div/table/thead/tr/th[5]')
    table = s.get_text_by_class('table')
    s.quit()
    creatures = get_creatures(BeautifulSoup(table, "lxml"))
    write_to_file(dir, creatures)

def take_creature_screenshots(image_dir, path_to_csv):
    s = Scraper('https://www.jsigvard.com/dnd/Monsters.html', './chromedriver')

    master = Master(get_creatures_from_csv(path_to_csv))

    creature_urls = {}
    for c in master.creatures:
        creature_urls.update({c.name:c.href})
    count = 0
    for name, url in creature_urls.items():
        count+=1
        s.driver.get(url)
        s.take_screen_shot_by_class_name("container", f"{image_dir}/{name}.png")
        

