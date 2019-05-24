from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobect import *
from PPlay.animation import *

class Player():
    def __init__(self, direcao):
        self.idle_direita = Animation("assets/player-idle-right.png", 4)
        self.idle_esquerda = Animation("assets/player-idle-left.png", 4)
        self.andando_direita = Animation("assets/player-walking-right.png", 8)
        self.andando_esquerda = Animation("assets/player-walking-left.png", 8)
        self.atacando_esquerda = Animation("assets/player-attack-left.png", 4)
        self.atacando_direita = Animation("assets/player-attack-right.png", 4)

        self.idle_direita.set_total_duration(800)
        self.idle_esquerda.set_total_duration(800)
        self.andando_direita.set_total_duration(800)
        self.andando_esquerda.set_total_duration(800)
        self.atacando_direita.set_total_duration(800)
        self.atacando_esquerda.set_total_duration(800)

        self.direcao = direcao


    def andarDireita(self, player, direcao):
        self.player = self.andando_direita
        self.player.x += 0.1
        self.idle_direita.x += 0.1
        self.idle_esquerda.x += 0.1
        self.andando_esquerda.x += 0.1
        self.atacando_esquerda.x += 0.1
        self.atacando_direita.x += 0.1
        direcao = 1
        return direcao

    def andarEsquerda(self):
        self.player = self.andando_esquerda
        self.player.x -= 0.1
        self.idle_direita.x -= 0.1
        self.idle_esquerda.x -= 0.1
        self.andando_direita.x -= 0.1
        self.atacando_esquerda.x-= 0.1
        self.atacando_direita.x -= 0.1
        direcao = 0
        return direcao

    def idle(self):
        if(self.direcao == 1):
            self.player = self.idle_direita
        elif(self.direcao == 0):
            self.player = self.idle_esquerda

    def andarDireitaBaixo(self):
            self.player = self.andando_direita
            self.player.y += 0.08
            self.idle_direita.y += 0.08
            self.idle_esquerda.y += 0.08
            self.andando_esquerda.y += 0.08
            self.atacando_esquerda.y += 0.08
            self.atacando_direita.y += 0.08
    def andarEsquerdaBaixo(self):
            self.player = self.andando_esquerda
            self.player.y += 0.08
            self.idle_direita.y += 0.08
            self.idle_esquerda.y += 0.08
            self.andando_direita.y += 0.08
            self.atacando_esquerda.y += 0.08
            self.atacando_direita.y += 0.08
    def andarDireitaCima(self):
            self.player = self.andando_direita
            self.player.y -= 0.08
            self.idle_direita.y -= 0.08
            self.idle_esquerda.y -= 0.08
            self.andando_esquerda.y -= 0.08
            self.atacando_esquerda.y -= 0.08
            self.atacando_direita.y -= 0.08
    def andarEsquerdaCima(self):
            self.player = self.andando_esquerda
            self.player.y -= 0.08
            self.idle_direita.y -= 0.08
            self.idle_esquerda.y -= 0.08
            self.andando_direita.y -= 0.08
            self.atacando_esquerda.y -= 0.08