from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
from player import Player
from enemy import Enemy1
from enemy_controller import Enemy_Controller
import globals

class Jogo(object):
    def __init__(self, janela):
        self.janela = janela
        self.teclado = janela.get_keyboard()
        self.player = Player(self.janela)
        self.enemyController = Enemy_Controller(3, self.janela, self.player)
        self.background = Sprite("assets/bg-fase1.png", 1)
        self.vidaHud = Animation("assets/vida_hud.png", 11)
        self.vida = 75
        self.pontuacao = 250000
        self.wave = 0
        self.set_pos()

    #Deve ser chamado quando o player toma um hit para não gastar processamento atoa
    def atualizaHudVida(self):
        if 90 < (self.vida) <= 100:
            self.vidaHud.set_curr_frame(0)
        elif 80 < (self.vida) <= 90:
            self.vidaHud.set_curr_frame(1)
        elif 70 < (self.vida) <= 80:
            self.vidaHud.set_curr_frame(2)
        elif 60 < (self.vida) <= 70:
            self.vidaHud.set_curr_frame(3)
        elif 50 < (self.vida) <= 60:
            self.vidaHud.set_curr_frame(4)
        elif 40 < (self.vida) <= 50:
            self.vidaHud.set_curr_frame(5)
        elif 30 < (self.vida) <= 40:
            self.vidaHud.set_curr_frame(6)
        elif 20 < (self.vida) <= 30:
            self.vidaHud.set_curr_frame(7)
        elif 10 < (self.vida) <= 20:
            self.vidaHud.set_curr_frame(8)
        elif 0 < (self.vida) <= 10:
            self.vidaHud.set_curr_frame(9)
        elif(self.vida)<=0:
            self.vidaHud.set_curr_frame(10)

    def set_pos(self):
        self.vidaHud.set_position(40, 40)

    def _draw(self):
        self.background.draw()
        self.vidaHud.draw()
        self.janela.draw_text(str(self.pontuacao) + " pts", self.janela.width - 200, 40, size=30, color=(255, 255, 255), font_name="Minecraft")


    def run(self):

        if(self.teclado.key_pressed("ESC")):
            globals.GAME_STATE = 1
        self.atualizaHudVida()
        self._draw()
        self.player.run()
