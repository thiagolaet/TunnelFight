from nave import *
from game_controller import *
from PPlay.window import *
from PPlay.sprite import *
import time

gc = GameController(800, 600, 3)

janela = Window(gc.width, gc.height)

tec = Window.get_keyboard()

#INPUT CONTROLLER
l_was_pressed = False
r_was_pressed = False

nave = Nave(gc.size, Sprite("sprites/nave.png"), janela.width, gc)
nave.sprite.y = janela.height - 10 -  nave.sprite.height
nave.position_nave()

while True:

    if tec.key_pressed("RIGHT") and not r_was_pressed:
        nave.setPosition("+")
        last_time = time.time()

    if tec.key_pressed("LEFT") and not l_was_pressed:
        nave.setPosition("-")
        last_time = time.time()

    janela.set_background_color((0, 0, 0))
    nave.update()
    r_was_pressed = tec.key_pressed("RIGHT")
    l_was_pressed = tec.key_pressed("LEFT")
    janela.update()
