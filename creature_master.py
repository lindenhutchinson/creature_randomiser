import random

class Creature:
    def __init__(self, name, cr, href, ctype):
        self.name = name
        self.cr = cr
        self.href = href
        self.ctype = ctype

    def to_string(self):
        return(f"{self.name},{self.cr},{self.href},{self.ctype}")


class Master:
    def __init__(self, creatures):
        self.creatures = creatures
    
    def get_all_cr(self):
        cr_list=[]
        for creature in self.creatures:
            if not creature.cr in cr_list:
                cr_list.append(creature.cr)

        return cr_list

    def get_all_type(self):
        type_list=[]
        for creature in self.creatures:
            if not creature.ctype in type_list:
                type_list.append(creature.ctype)

        return type_list

    def get_possible_creatures_string(self, cr, ctype):
        num = len(self.get_possible_creatures(cr, ctype))
        return f"There {'are' if num != 1 else 'is'} {num} {ctype.lower()}{'s' if ctype!='Fey' and num != 1 else ''} that {'are' if num != 1 else 'is'} CR {cr}"

    def get_possible_creatures(self, cr, ctype):
        return [c for c in self.creatures if c.cr == cr and c.ctype == ctype]

    def get_random_creatures(self, num, cr, ctype):
        possible = self.get_possible_creatures(cr, ctype)
        if not possible:
            return
        creatures = {}

        for _ in range(0, num):
            rando = random.choice(possible).name
            if rando in creatures.keys():
                creatures[rando]+=1
            else:
                creatures.update({rando:1})

        return creatures



