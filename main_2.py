import time
from Class_RPC import Game


def main():
    '''Rock, paper, Scissors simple game.
    Coded by Salaheldin Khaled on 14/12/2017'''
    newPlayer = Game()
    playerName = raw_input(
        '''Hello to Rock, Paper, Scissors.
    Please input player name: ''')
    print 'Hello {}, are you ready? Game on!'.format(playerName), '\n'
    time.sleep(2.5)
    gameOver = False
    while not gameOver:
        playerChoise = input('''Please choose a number from
        1. paper
        2. rock
        3. scissors
        Your Number: ''')
        print 'You chose {}'.format(newPlayer.player(playerChoise))
        print ' CPU will now choose randomly!'
        cpu = newPlayer.computer()
        user = newPlayer.player(playerChoise)
        print '  CPU chose {}'.format(cpu), '\n'
        time.sleep(2)
        print newPlayer.rules(user, cpu), '\n'
        endGame = raw_input('''do you want to play another round?
        please input
        y for yes
        any other key for exit:''')
        if endGame == 'y':
            continue
        else:
            gameOver = True
    print 'Game over!'


if __name__ == "__main__":
    main()
