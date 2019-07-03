from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.mouse import Mouse
from PPlay.animation import *
import globals

class Menu(object):
    def __init__(self, janela):
        self.janela = janela
        self.distancia = 60
        self.arcade = Sprite("assets/botao_arcade.png")
        self.arcadeHover = Sprite("assets/botao_arcadehover.png")
        self.sair = Sprite("assets/botao_sair.png")
        self.sairHover = Sprite("assets/botao_sairhover.png")
        self.ranking = Sprite("assets/botao_ranking.png")
        self.rankingHover = Sprite("assets/botao_rankinghover.png")

        self.mouse = Mouse()
        self.set_pos()
        self._draw()

    def set_pos(self):
        self.arcade.set_position(self.janela.width/2 - self.arcade.width/2, self.distancia)
        self.arcadeHover.set_position(self.janela.width/2 - self.arcade.width/2, self.distancia)
        self.ranking.set_position(self.janela.width/2 - self.ranking.width/2, 2 * self.distancia + self.arcade.height)
        self.rankingHover.set_position(self.janela.width/2 - self.ranking.width/2, 2 * self.distancia + self.arcade.height)
        self.sair.set_position(self.janela.width/2 - self.sair.width/2, 3 * self.distancia + self.arcade.height + self.ranking.height)
        self.sairHover.set_position(self.janela.width/2 - self.sair.width/2, 3 * self.distancia + self.arcade.height + self.ranking.height)


    def _draw(self):
        self.arcade.draw() 
        self.sair.draw() 
        self.ranking.draw()

    def run(self):
        self.janela.set_background_color((0, 0, 0))
        self._draw()
        self.set_pos()

        if(self.mouse.is_over_object(self.arcade)):
            self.arcadeHover.draw()
            if(self.mouse.is_button_pressed(1)):
                globals.GAME_STATE = 2

        elif(self.mouse.is_over_object(self.ranking)):
            self.rankingHover.draw()
            if(self.mouse.is_button_pressed(1)):
                globals.GAME_STATE = 3

        elif(self.mouse.is_over_object(self.sair)):
            self.sairHover.draw()
            if(self.mouse.is_button_pressed(1)):
                globals.GAME_STATE = 4
        
        