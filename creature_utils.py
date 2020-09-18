from bs4 import BeautifulSoup
from scraper import Scraper
from master import Master, Creature
  


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
    master = Master()
    master.creatures = get_creatures(BeautifulSoup(table, "lxml"))
    master.write_to_file(dir)


    # parse data from https://dnd-wiki.org
    # def get_better_creatures(self):
    #     rows = self.soup.find_all('tr')
    #     creatures = []
    #     for row in rows[1:]:
    #         data = row.find_all('td')
    #         print(data[3].get_text())
    #         break
    #         if(data[1] =='Beast'):
    #             name = data[0].get_text()
    #             if 'Campaign Setting' in name:
    #                 continue
    #             href = 'https://dnd-wiki.org'+data[0].find('a').get('href')
    #             cr = data[5].get_text()
                
    #             creatures.append(Creature(name, cr, href))

    #     return creatures