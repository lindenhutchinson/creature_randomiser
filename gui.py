from creatures import Master
import easygui
import sys


class Gui:
    def __init__(self, master):
        self.master = master
        self.cr = -1
        self.num = 0

    def main(self):
        while 1:
            self.home()

    def home(self):
        msg = ''
        if self.num > 0 and self.cr != -1:
            msg += self.master.get_random_creatures_string(self.num, self.cr)

        if self.num > 0:
            msg+=f"\n\nNum: {self.num}"
        if self.cr != -1:
            msg+=f"\n\nCR: {self.cr}"

        choices = ['Change CR','Randomise Creatures', 'Change Number of Creatures']
        action = easygui.buttonbox(msg=msg, title="Get Random Creatures", choices=choices)
        if action == 'Change CR':
            self.get_cr()
        elif action == 'Change Number of Creatures':
            self.get_num()
        elif action == 'Randomise Creatures':
            if self.num == 0 or self.cr == -1:
                self.get_cr()
                self.get_num()
            else:
                self.home()
            

    def get_cr(self):
        msg = 'Select the cr of the creatures you are randomizing'
        choices = ['0', '1/8', '1/4','1/2', '1', '2','3','4','5','6','7']
        self.cr=easygui.buttonbox(msg=msg, title='What cr are these creatures?', choices=choices)

    def get_num(self):
        msg = 'Select the number of the creatures you are randomizing'
        choices = [1,2,3,4,5,6,7,8]
        choices = [str(i) for i in choices]
        self.num=int(easygui.buttonbox(msg=msg, title='How many creatures?', choices=choices))


        # if(choice == "Clear Selected Dice"):
        #     self.player.clear_dice()
        # elif(choice == "Roll Dice"):
        #     self.player.get_rolls()
        # elif(choice is None):
        #     sys.exit(0)
        # else:
        #     self.player.add_die(Dice[choice].value)

