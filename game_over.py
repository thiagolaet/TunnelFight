from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.mouse import Mouse
from PPlay.animation import *
import globals

class GameOver(object):
    def __init__(self, janela):
        self.janela = janela
        self.distancia = 60
        self.pontuacao = 0
        self.background = Sprite("assets/bg-fase1-menu.png")
        self.bg = Sprite("assets/background-gameover.png")

        self.mouse = Mouse()
        self.set_pos()
        self._draw()

    def set_pos(self):
        self.bg.set_position(self.janela.width/2 - self.bg.width/2, self.janela.height/2 - self.bg.height/2)


    def _draw(self):
        self.background.draw()
        self.bg.draw()


    def run(self, pontuacao):
        self._draw()
        self.set_pos()
        self.pontuacao = pontuacao
        self.janela.draw_text("Pontuação: "+str(self.pontuacao), self.janela.width/2, self.janela.height/2, size=30, color=(255, 255, 255), font_name="Minecraft")

        if self.janela.get_keyboard().key_pressed("ESC"):
            globals.GAME_STATE = 1
        