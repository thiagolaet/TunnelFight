from enemy import*
from random import randrange
class Enemy_Controller():
    def __init__(self, strt, janela, player):
        self.enemyList = []
        self.startEnemies = strt
        for a in range(self.startEnemies):
            if a % 2 == 0:
                pos = randrange(0, janela.width)
                temp = Enemy1(janela, player, pos, janela.height)
            else:
                pos = randrange(int(janela.height/2), janela.height)
                temp = Enemy1(janela, player, janela.width, pos)
            self.enemyList.append(temp)


