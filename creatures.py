from bs4 import BeautifulSoup
import random

class Creature:
    def __init__(self, name, cr, href, ctype):
        self.name = name
        self.cr = cr
        self.href = href
        self.ctype = ctype

    def to_string(self):
        return(f"{self.name},{self.cr},{self.href},{self.ctype}")

    def to_print(self):
        return(f"{self.name} - {self.href}\n\n")

class Master:
    def __init__(self, creatures):
        self.creatures = creatures

    def write_to_file(self, dir):
        with open(dir, 'w', encoding="utf-8") as fn:
            for creature in self.creatures:
                fn.write(creature.to_string()+'\n')

    def get_possible_creatures(self, cr, ctype):
        return [c for c in self.creatures if c.cr == cr and c.ctype == ctype]

    def get_random_creatures(self, num, cr, ctype):
        possible = self.get_possible_creatures(cr, ctype)

        creatures = {}

        for _ in range(0, num):
            rando = random.choice(possible).to_print()
            if rando in creatures.keys():
                creatures[rando]+=1
            else:
                creatures.update({rando:1})

        return creatures

    def get_random_creatures_string(self, num, cr, ctype):
        creatures = self.get_random_creatures(num, cr, ctype)
        msg = ''
        for creature, num in creatures.items():
            msg += f"{num} x {creature}\n"

        return msg


class CreatureParser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "lxml")

    def get_creatures(self):
        rows = self.soup.find_all('tr')
        creatures = []
        for row in rows[2:]:
            data = row.find_all('td')
            ctype = data[2].get_text()
            if ctype in ['Beast', 'Fey', 'Elemental']:
                name = data[0].get_text()
                href = 'https://www.jsigvard.com/dnd/'+data[0].find('a').get('href')
                cr = str(data[4].contents[1])
            
                creatures.append(Creature(name, cr, href, ctype))

        return creatures
    # def get_creatures(self):
    #     rows = self.soup.find_all('tr')
    #     creatures = []
    #     for row in rows[1:]:
    #         data = row.find_all('td')
    #         name = data[0].get_text()
    #         if 'Campaign Setting' in name:
    #             continue
    #         href = 'https://dnd-wiki.org'+data[0].find('a').get('href')
    #         cr = data[5].get_text()
            
    #         creatures.append(Creature(name, cr, href))

    #     return creatures


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