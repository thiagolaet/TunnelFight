from enemy import*
from random import randrange
class Enemy_Controller():
    def __init__(self, janela, player):
        self.enemyList = []
        self.player = player
        self.janela = janela


    def list_control(self):
        for a in range(len(self.enemyList)):
            if not self.enemyList[a].life.alive:
                self.enemyList.pop(a)
                break

    def start_a_wave(self, nmbr):
        if len(self.enemyList) == 0:
            for a in range(nmbr):
                pos = randrange(self.janela.height / 2, self.janela.height)
                if a % 2 == 0:
                    temp = Enemy1(self.janela, self.player, -100, pos)
                else:
                    temp = Enemy1(self.janela, self.player, self.janela.width, pos)
                self.enemyList.append(temp)


    def run(self):
        self.list_control()
        for a in self.enemyList:
            a.run(self.player)
