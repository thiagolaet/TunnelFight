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
from sound_controller import*
from game_over import*
import globals

janela = Window(globals.WIDTH, globals.HEIGHT)
teclado = janela.get_keyboard()
janela.set_title("Tunnel Fight")

s_c = Sound_controller()
gameover = GameOver(janela)
jogo = Jogo(janela)
menu = Menu(janela)
ranking = Ranking(janela)

while True:
    if(globals.GAME_STATE == 1):
        menu.run()
        if jogo.jogando == False:
            jogo = Jogo(janela)
    elif(globals.GAME_STATE == 2):    
        jogo.run()
    elif(globals.GAME_STATE == 3):
        ranking.run()
    elif globals.GAME_STATE == 4:
        gameover.run(jogo.gameController.pontuacao, jogo.gameController.current_wave)
    elif globals.GAME_STATE == 15:
        break

    else:
        globals.GAME_STATE = 1

    if globals.GAME_STATE != 4:
        s_c.gameover.stop()
        s_c.tema.play()
    else:
        s_c.tema.stop()
        s_c.gameover.play()
    janela.update()