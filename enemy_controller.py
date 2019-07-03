from enemy import*
from random import randrange
class Enemy_Controller():
    def __init__(self, strt, janela, player):
        self.enemyList = []
        self.startEnemies = strt
        self.player = player
        for a in range(self.startEnemies):
            #pos = randrange(janela.height / 2, janela.height)
            pos = 10
            if a % 2 == 0:
                temp = Enemy1(janela, player, -100, pos)
            else:
                temp = Enemy1(janela, player, janela.width, pos)
            print(pos)
            self.enemyList.append(temp)


    def draw(self):
        for a in self.enemyList:
            a.enemy.draw()

    '''def checar_iguais(self):
        for a in range(len(self.enemyList)):
            for b in range(a, len(self.enemyList)):
                if self.enemyList[a].enemy.x == self.enemyList[b].enemy.x and self.enemyList[a].enemy.y == self.enemyList[b].enemy.y:
                    self.enemyList[b].enemy.x += 10'''

    def run(self):
        self.draw()
        self.checar_iguais()
        for a in self.enemyList:
            a.run(self.player)
