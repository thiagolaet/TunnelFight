from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *

janela = Window(1000, 800)
teclado = janela.get_keyboard()
janela.set_title("Daft Drunk")    

background = Sprite("assets/background.png", 1)

frame_per_SECOND = 60
speed_per_FRAME = 60

#player
idle_direita = Animation("assets/player-idle-right-2.png", 4)
idle_esquerda = Animation("assets/player-idle-left-2.png", 4)
andando_direita = Animation("assets/player-walking-right-2.png", 8)
andando_esquerda = Animation("assets/player-walking-left-2.png", 8)
atacando_esquerda = Animation("assets/player-attack-left.png", 4)
atacando_direita = Animation("assets/player-attack-right2.png", 9)

idle_direita.set_total_duration(800)
idle_esquerda.set_total_duration(3000)
andando_direita.set_total_duration(800)
andando_esquerda.set_total_duration(800)
atacando_direita.set_total_duration(800)
atacando_esquerda.set_total_duration(800)

player = idle_direita

player.set_position(100, janela.height - 100)
atacando_direita.set_position(100, janela.height - 100)
atacando_direita.set_position(100, janela.height - 100)
andando_esquerda.set_position(100, janela.height - 100)
andando_direita.set_position(100, janela.height - 100)
idle_esquerda.set_position(100, janela.height - 100)


direcao = 1
#1 = direita / 2 = esquerda

while True:
    janela.set_background_color((255,255,255))
    background.draw()
    if(teclado.key_pressed("D")):
        player = andando_direita
        player.x += 0.4
        idle_direita.x += 0.4
        idle_esquerda.x += 0.4
        andando_esquerda.x += 0.4
        atacando_esquerda.x += 0.4
        atacando_direita.x += 0.4
        direcao = 1
    elif(teclado.key_pressed("A")):
        player = andando_esquerda
        player.x -= 0.4
        idle_direita.x -= 0.4
        idle_esquerda.x -= 0.4
        andando_direita.x -= 0.4
        atacando_esquerda.x-= 0.4
        atacando_direita.x -= 0.4
        direcao = 0
    else: 
        if(direcao == 1):
            player = idle_direita
        elif(direcao == 0):
            player = idle_esquerda

    if(teclado.key_pressed("S")):
        if(direcao == 1):
            player = andando_direita
            player.y += 0.4
            idle_direita.y += 0.4
            idle_esquerda.y += 0.4
            andando_esquerda.y += 0.4
            atacando_esquerda.y += 0.4
            atacando_direita.y += 0.4
        else:
            player = andando_esquerda
            player.y += 0.4
            idle_direita.y += 0.4
            idle_esquerda.y += 0.4
            andando_direita.y += 0.4
            atacando_esquerda.y += 0.4
            atacando_direita.y += 0.4

    if(teclado.key_pressed("W")):
        if(direcao == 1):
            player = andando_direita
            player.y -= 0.4
            idle_direita.y -= 0.4
            idle_esquerda.y -= 0.4
            andando_esquerda.y -= 0.4
            atacando_esquerda.y -= 0.4
            atacando_direita.y -= 0.4
        else:
            player = andando_esquerda
            player.y -= 0.4
            idle_direita.y -= 0.4
            idle_esquerda.y -= 0.4
            andando_direita.y -= 0.4
            atacando_esquerda.y -= 0.4

    if(teclado.key_pressed("I")):
        if direcao == 1:
            player = atacando_direita
        else:
            player = atacando_esquerda

    player.draw()
    player.update()
    janela.update()