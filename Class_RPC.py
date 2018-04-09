import random


class Game:
    def computer(self):
        choice = random.choice(('rock', 'paper', 'scissors'))
        return choice

    def player(self, playerChoise):
        self.playerChoise = playerChoise
        if playerChoise == 1:
            return 'paper'
        elif playerChoise == 2:
            return 'rock'
        else:
            return 'scissors'

    def rules(self, user, cpu):
        self.user = user
        self.cpu = cpu
        if user == cpu:
            return 'Tie'
        elif (user, cpu) in (('rock', 'scissors'),
                             ('paper', 'rock'),
                             ('scissors', 'paper')):
            return 'Congratulation, You won'
        else:
            return 'Hard-luck, CPU won'
