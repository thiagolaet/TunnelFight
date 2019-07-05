from enemy import*
from random import randrange
class Enemy_Controller():
    def __init__(self, janela, player):
        self.enemyList = []
        self.dieList = []
        self.player = player
        self.janela = janela

    def novaMorte(self, inimigo):
        self.dieList.append(Animation("assets/enemy_dying.png", 28))
        self.dieList[len(self.dieList)-1].set_position(inimigo.enemy.x, inimigo.enemy.y)
        self.dieList[len(self.dieList)-1].set_sequence_time(0, 14, 100)
        self.dieList[len(self.dieList)-1].set_sequence_time(14, 28, 100)

        if inimigo.direcao == 1:
            self.dieList[len(self.dieList)-1].set_sequence(0, 14)
        elif inimigo.direcao == 2:
            self.dieList[len(self.dieList)-1].set_sequence(14, 28)

    def atualizaMorte(self):
        for i in range(len(self.dieList)):
            self.dieList[i].update()
            if self.dieList[i].get_curr_frame() == 13 or self.dieList[i].get_curr_frame() == 27:
                self.dieList.pop(i)
                break

    def list_control(self):
        for a in range(len(self.enemyList)):
            if not self.enemyList[a].life.alive:
                self.novaMorte(self.enemyList[a])
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
