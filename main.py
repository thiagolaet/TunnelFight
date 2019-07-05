from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
from player import Player
from enemy import Enemy1
<<<<<<< HEAD
from menu import Menu
from jogo import Jogo
from ranking import Ranking
=======
from enemy_controller import*
from game_controller import*
>>>>>>> gaid
import globals

janela = Window(globals.WIDTH, globals.HEIGHT)
teclado = janela.get_keyboard()
janela.set_title("Daft Drunk")    

<<<<<<< HEAD
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
    
=======
fase = 1

background = Sprite("assets/bg-fase1.png", 1)
player = Player(janela)
enemy1 = Enemy1(janela, player, 700, 340)
enemy2 = Enemy1(janela, player, 600, 390)
enemy3 = Enemy1(janela, player, 800, 390)
enemy4 = Enemy1(janela, player, 700, 440)

enemy_controller = Enemy_Controller(4, janela, player)
gc = GameController(player, enemy_controller)


while True:
    background.draw()
    #checarLimitesJogador()
    player.run()
    enemy_controller.run()
    gc.run()
>>>>>>> gaid
    janela.update()