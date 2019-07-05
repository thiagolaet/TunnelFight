from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
from player import Player
from enemy import Enemy1
from enemy_controller import*
from game_controller import*
import globals

janela = Window(globals.WIDTH, globals.HEIGHT)
teclado = janela.get_keyboard()
janela.set_title("Daft Drunk")    

fase = 1

background = Sprite("assets/bg-fase1.png", 1)
player = Player(janela)
enemy1 = Enemy1(janela, player, 700, 340)
enemy2 = Enemy1(janela, player, 600, 390)
enemy3 = Enemy1(janela, player, 800, 390)
enemy4 = Enemy1(janela, player, 700, 440)

enemy_controller = Enemy_Controller(janela, player)
gc = GameController(4, player, enemy_controller, janela)


while True:
    background.draw()
    #checarLimitesJogador()
    player.run()
    enemy_controller.run()
    gc.run()
    janela.update()