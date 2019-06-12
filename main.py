from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
from player import Player
import globals


janela = Window(globals.WIDTH, globals.HEIGHT)
teclado = janela.get_keyboard()
janela.set_title("Daft Drunk")    

background = Sprite("assets/background.png", 1)

direcao = 1
#1 = direita / 2 = esquerda

player = Player(janela)

def checarLimitesJogador():
    if player.player.y < 260:
        player.set_pos_y(260)
    if player.player.y > 470:
        player.set_pos_y(470)

while True:
    background.draw()
    
    checarLimitesJogador()
    player.run()
    janela.update()