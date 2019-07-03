from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
from player import Player
from enemy import Enemy1
from menu import Menu
from jogo import Jogo
from ranking import Ranking
import globals

janela = Window(globals.WIDTH, globals.HEIGHT)
teclado = janela.get_keyboard()
janela.set_title("Daft Drunk")    

jogo = Jogo(janela)
menu = Menu(janela)
ranking = Ranking(janela)

while globals.GAME_STATE != 4:
    if(globals.GAME_STATE == 1):
        menu.run()
    elif(globals.GAME_STATE == 2):    
        jogo.run()
    elif(globals.GAME_STATE == 3):
        ranking.run()
    
    janela.update()