from bs4 import BeautifulSoup
import random

class Creature:
    def __init__(self, name, cr, href):
        self.name = name
        self.cr = cr
        self.href = href

    def to_string(self):
        return(f"{self.cr}  {self.name} - {self.href}")


class Master:
    def __init__(self, creatures):
        self.creatures = creatures

    def print_creatures(self):
        for c in self.creatures:
            print(c.to_string())

    def write_to_file(self, dir):
        with open(dir, 'w', encoding="utf-8") as fn:
            for creature in self.creatures:
                fn.write(creature.to_string())
                fn.write('\n')

    def get_possible_creatures(self, cr):
        return [c for c in self.creatures if c.cr == cr]

    def print_choice(self, cr, num, len):
        print(f"Picking {num} times from {len} possible creatures with cr {cr}")

    def get_random_creature(self):
        # self.print_choice('any', 1, len(self.creatures))
        print(random.choice(self.creatures).to_string())

    def get_random_creature_cr(self, cr):
        possible = self.get_possible_creatures(cr)
        self.print_choice(cr, 1, len(possible))
        print(random.choice(possible).to_string())

    def get_random_creatures(self, num, cr):
        possible = self.get_possible_creatures(cr)
        # self.print_choice(cr, num, len(possible))
        creatures = []
        seen_creatures = []
        for i in range(0, num):
            rando = random.choice(possible).to_string()
            if rando in seen_creatures:
                creatures.insert(creatures.index(rando), rando)
            else:
                creatures.append(rando)
                seen_creatures.append(rando)

        return creatures

    def get_random_creatures_string(self, num, cr):
        creatures = self.get_random_creatures(num, cr)
        msg = ''
        for c in creatures:
            msg+=f"{c}\n"

        return msg


class CreatureParser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "lxml")

    def get_creatures(self):
        rows = self.soup.find_all('tr')
        creatures = []
        for row in rows[1:]:
            data = row.find_all('td')
            name = data[0].get_text()
            if 'Campaign Setting' in name:
                continue
            href = 'https://dnd-wiki.org'+data[0].find('a').get('href')
            cr = data[5].get_text()
            
            creatures.append(Creature(name, cr, href))

        return creatures