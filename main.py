from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
from player import Player
from enemy import Enemy1
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



while True:
    background.draw()
    #checarLimitesJogador()
    enemy1.run()
    enemy2.run()
    enemy3.run()
    enemy4.run()
    player.run()

    janela.update()