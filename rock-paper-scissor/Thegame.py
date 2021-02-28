import random
class Thegame():
    def __init__(self):
        self.ava_opt = ['rock', 'paper', 'scissor']
        self.user_choice = self.init_user()
        self.get_the_winner()
            
    
    def init_user(self):
        usr_chice = str(input('your choice : '))
        return usr_chice

    def set_winner(self, winner):
        print('{}'.format(winner))


    def get_the_winner(self):
        comp_choice = random.choice(self.ava_opt)
        print('computer choice : ', comp_choice)

        if comp_choice == 'rock':
            if self.user_choice == 'scissor':
                self.set_winner('computer wins')
            elif self.user_choice == 'paper':
                self.set_winner('user wins')
            else:
                self.set_winner('draw')
        
        elif comp_choice == 'paper':
            if self.user_choice == 'scissor':
                self.set_winner('user wins')
            elif self.user_choice == 'rock':
                self.set_winner('computer wins')
            else:
                self.set_winner('draw')
        else: 
            if self.user_choice == 'rock':
                self.set_winner('user wins')
            elif self.user_choice == 'paper':
                self.set_winner('computer wins')
            else:
                self.set_winner('draw')





                






