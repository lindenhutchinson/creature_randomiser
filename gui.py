from creatures import Master
import easygui
import sys

CR_LIST = ['0', '1/8', '1/4','1/2', '1', '2','3','4','5','6','7']
CREATURE_TYPES = ['Fey', 'Elemental', 'Beast']
VALID_CREATURE_NUMBERS = [1,2,3,4,5,6,7,8]

class Gui:
    def __init__(self, master):
        self.master = master
        self.cr = -1
        self.num = -1
        self.ctype = -1

    def main(self):
        while 1:
            self.home()

    def home(self):
        msg = ''
        # if self.num > 0 and self.cr != -1 and self.ctype!= '':
        if -1 not in (self.num, self.cr, self.ctype):
            msg += self.master.get_random_creatures_string(self.num, self.cr, self.ctype)

        if self.num != -1:
            msg+=f"\n\nNum: {self.num}"
        if self.cr != -1:
            msg+=f"\n\nCR: {self.cr}"
        if self.ctype != -1:
            msg+=f"\n\nType: {self.ctype}"

        choices = ['Change CR','Change Type','Change Num', 'Randomize Creatures']
        action = easygui.buttonbox(msg=msg, title="Get Random Creatures", choices=choices)
        if action == 'Change CR':
            self.get_cr()
        elif action == 'Change Type':
            self.get_type()
        elif action == 'Change Num':
            self.get_num()
        elif action == 'Randomize Creatures':
            # if self.num == 0 or self.cr == -1 or self.ctype == '':
            if -1 in (self.num, self.cr, self.ctype):
            
                self.get_cr()
                self.get_num()
                self.get_type()
            else:
                self.home()
        

    def get_type(self):
        msg = 'What type are your creatures?'
        choices = CREATURE_TYPES
        self.ctype=easygui.buttonbox(msg=msg, title='What type are these creatures?', choices=choices)  

    def get_cr(self):
        msg = 'Select the cr of the creatures you are randomizing'
        choices = CR_LIST
        self.cr=easygui.buttonbox(msg=msg, title='What cr are these creatures?', choices=choices)

    def get_num(self):
        msg = 'Select the number of the creatures you are randomizing'
        choices = VALID_CREATURE_NUMBERS
        choices = [str(i) for i in choices]
        self.num=int(easygui.buttonbox(msg=msg, title='How many creatures?', choices=choices))

