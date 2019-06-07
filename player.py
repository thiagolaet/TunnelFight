from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *

class Player():
    def __init__(self, janela):
        self.idle_direita = Animation("assets/player-idle-right-2.png", 4)
        self.idle_esquerda = Animation("assets/player-idle-left-2.png", 4)
        self.andando_direita = Animation("assets/player-walking-right-2.png", 8)
        self.andando_esquerda = Animation("assets/player-walking-left-2.png", 8)
        self.atacando_esquerdaI = Animation("assets/player-attack-left-2.png", 9)
        self.atacando_direitaI = Animation("assets/player-attack-right-2.png", 9)
        self.player = self.idle_direita = Animation("assets/player-idle-right-2.png", 4)
        self.idle_direita.set_total_duration(800)
        self.idle_esquerda.set_total_duration(800)
        self.andando_direita.set_total_duration(800)
        self.andando_esquerda.set_total_duration(800)
        self.atacando_direitaI.set_total_duration(800)
        self.atacando_esquerdaI.set_total_duration(800)
        self.janela = janela
        self.teclado = janela.get_keyboard()
        self.direcao = 1
        self.set_pos(100, self.janela.height - 200)

        self.contador = 0
        #1 - pode fazer tudo / 2 - tem que esperar a animação atual acabar
        self.estado = 1
        self.vida = 50


    def set_pos(self, x, y):
        self.player.set_position(x, y)
        self.atacando_direitaI.set_position(x, y)
        self.atacando_esquerdaI.set_position(x, y)
        self.andando_esquerda.set_position(x, y)
        self.andando_direita.set_position(x, y)
        self.idle_esquerda.set_position(x, y)

    def set_pos_y(self, y):
        self.player.set_position(self.player.x, y)
        self.atacando_direitaI.set_position(self.player.x, y)
        self.atacando_esquerdaI.set_position(self.player.x, y)
        self.andando_esquerda.set_position(self.player.x, y)
        self.andando_direita.set_position(self.player.x, y)
        self.idle_esquerda.set_position(self.player.x, y)
        self.idle_direita.set_position(self.player.x, y)

    def andarDireita(self):
        self.player = self.andando_direita
        self.player.x += 0.4
        self.idle_direita.x += 0.4
        self.idle_esquerda.x += 0.4
        self.andando_esquerda.x += 0.4
        self.atacando_esquerdaI.x += 0.4
        self.atacando_direitaI.x += 0.4
        self.direcao = 1

    def andarEsquerda(self):
        self.player = self.andando_esquerda
        self.player.x -= 0.4
        self.idle_direita.x -= 0.4
        self.idle_esquerda.x -= 0.4
        self.andando_direita.x -= 0.4
        self.atacando_esquerdaI.x-= 0.4
        self.atacando_direitaI.x -= 0.4
        self.direcao = 0

    def idle(self):
        if(self.direcao == 1):
            self.player = self.idle_direita
        elif(self.direcao == 0):
            self.player = self.idle_esquerda

    def andarDireitaBaixo(self):
            self.player = self.andando_direita
            self.player.y += 0.3
            self.idle_direita.y += 0.3
            self.idle_esquerda.y += 0.3
            self.andando_esquerda.y += 0.3
            self.atacando_esquerdaI.y += 0.3
            self.atacando_direitaI.y += 0.3
    def andarEsquerdaBaixo(self):
            self.player = self.andando_esquerda
            self.player.y += 0.3
            self.idle_direita.y += 0.3
            self.idle_esquerda.y += 0.3
            self.andando_direita.y += 0.3
            self.atacando_esquerdaI.y += 0.3
            self.atacando_direitaI.y += 0.3
    def andarDireitaCima(self):
            self.player = self.andando_direita
            self.player.y -= 0.3
            self.idle_direita.y -= 0.3
            self.idle_esquerda.y -= 0.3
            self.andando_esquerda.y -= 0.3
            self.atacando_esquerdaI.y -= 0.3
            self.atacando_direitaI.y -= 0.3
    def andarEsquerdaCima(self):
            self.player = self.andando_esquerda
            self.player.y -= 0.3
            self.idle_direita.y -= 0.3
            self.idle_esquerda.y -= 0.3
            self.andando_direita.y -= 0.3
            self.atacando_esquerdaI.y -= 0.3
            self.atacando_direitaI.y -= 0.3

    def atacarDireitaI(self):
        self.player = self.atacando_direitaI
        self.estado = 2
        self.contador = 0

    def atacarEsquerdaI(self):
        self.player = self.atacando_esquerdaI
        self.estado = 2
        self.contador = 0
    

    def run(self):
        self.player.draw()
        self.player.update()
        if self.estado != 2:
            if(self.teclado.key_pressed("D")):
                self.andarDireita()
            elif(self.teclado.key_pressed("A")):
                self.andarEsquerda()
            else: 
                self.idle()

            if(self.teclado.key_pressed("S")):
                if(self.direcao == 1):
                    self.andarDireitaBaixo()
                else:
                    self.andarEsquerdaBaixo()

            if(self.teclado.key_pressed("W")):
                if(self.direcao == 1):
                    self.andarDireitaCima()
                else:
                    self.andarEsquerdaCima()
            
            if(self.contador > 0.20):
                if(self.teclado.key_pressed("I")):
                    if(self.direcao == 1):
                        self.atacarDireitaI()
                    else:
                        self.atacarEsquerdaI()
        else:
            if self.contador > 0.7:
                self.estado = 1
                self.atacando_direitaI.set_curr_frame(0)
                self.atacando_esquerdaI.set_curr_frame(0)
                self.contador = 0

        self.contador += self.janela.delta_time()
