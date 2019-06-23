from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
import globals

class Player():
    def __init__(self, janela):
        self.janela = janela
        self.teclado = janela.get_keyboard()

        self.player = Animation("assets/player-animation-2.png", 76)
        self.player.set_position(100, self.janela.height - 200)
        self._set_seq_time()
        
        #1 = direita / 2 = esquerda
        self.direcao = 1

        #1 - idleRight / 1.5 - idleLeft / 2 - walkRight / 2.5 - walkLeft / 3 3.5 - attack1 / 4 4.5 - attack2 / 5 5.5 - attack3 / 6 6.5 - attack4  
        self.player_state = 1
        self.contador = 0
        self.player.set_sequence(0, 4)


    def _set_seq_time(self):
        self.player.set_sequence_time(0, 4, 200)    
        self.player.set_sequence_time(4, 8, 200)
        self.player.set_sequence_time(8, 16, 100)
        self.player.set_sequence_time(16, 24, 100)
        self.player.set_sequence_time(24, 28, 220)
        self.player.set_sequence_time(28, 32, 220)
        self.player.set_sequence_time(32, 37, 150)
        self.player.set_sequence_time(37, 42, 150)
        self.player.set_sequence_time(42, 51, 120)
        self.player.set_sequence_time(51, 60, 120)
        self.player.set_sequence_time(60, 68, 120)
        self.player.set_sequence_time(68, 76, 120)

    def idleRight(self):
        if self.player_state != 1:
            self.player.set_sequence(0, 4)
            self.player_state = 1

    def idleLeft(self):
        if self.player_state != 1.5:
            self.player.set_sequence(4, 8)
            self.player_state = 1.5

    def walkRight(self):
        if self.player_state != 2: 
            self.player.set_sequence(8, 16)
            self.player_state = 2
            self.player.y -= 0.2
            self.player.y += 0.2
        self.player.x += 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 1

    def walkRightUp(self):
        if self.player_state != 2: 
            self.player.set_sequence(8, 16)
            self.player_state = 2
        self.player.y -= 0.2        
        self.player.x += 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 1

    def walkRightDown(self):
        if self.player_state != 2: 
            self.player.set_sequence(8, 16)
            self.player_state = 2
        self.player.y += 0.2
        self.player.x += 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 1

    def walkLeft(self):
        if self.player_state != 2.5:
            self.player.set_sequence(16, 24)
            self.player_state = 2.5
        self.player.x -= 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 2
    
    def walkLeftUp(self):
        if self.player_state != 2.5:
            self.player.set_sequence(16, 24)
            self.player_state = 2.5
        self.player.y -= 0.2
        self.player.x -= 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 2

    def walkLeftDown(self):
        if self.player_state != 2.5:
            self.player.set_sequence(16, 24)
            self.player_state = 2.5
        self.player.y += 0.2
        self.player.x -= 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 2

    def walkUp(self):
        if self.direcao == 1:
            self.player.y -= 0.2
            if self.player_state != 2: 
                self.player.set_sequence(8, 16)
                self.player_state = 2
        if self.direcao == 2:
            self.player.y -= 0.2
            if self.player_state != 2.5: 
                self.player.set_sequence(16, 24)
                self.player_state = 2.5

    def walkDown(self):
        if self.direcao == 1:
            self.player.y += 0.2
            if self.player_state != 2: 
                self.player.set_sequence(8, 16)
                self.player_state = 2
        if self.direcao == 2:
            self.player.y += 0.2
            if self.player_state != 2.5: 
                self.player.set_sequence(16, 24)
                self.player_state = 2.5

    def weakPunch(self):
        if self.direcao == 1:
            if self.player_state != 3:
                self.player.set_sequence(24, 28)
                self.player.set_curr_frame(24)
                self.player_state = 3
                self.contador = 0
        elif self.direcao == 2:
            if self.player_state != 3.5:
                self.player.set_sequence(28, 32)
                self.player.set_curr_frame(28)
                self.player_state = 3.5
                self.contador = 0

    def weakKick(self):
        if self.direcao == 1:
            if self.player_state != 4:
                self.player.set_sequence(32, 37)
                self.player.set_curr_frame(32)
                self.player_state = 4
                self.contador = 0
        elif self.direcao == 2:
            if self.player_state != 4.5:
                self.player.set_sequence(37, 42)
                self.player.set_curr_frame(37)
                self.player_state = 4.5
                self.contador = 0

    def strongPunch(self):
        if self.direcao == 1:
            if self.player_state != 5:
                self.player.set_sequence(42, 51)
                self.player.set_curr_frame(42)
                self.player_state = 5
                self.contador = 0
        elif self.direcao == 2:
            if self.player_state != 5.5:
                self.player.set_sequence(51, 60)
                self.player.set_curr_frame(51)
                self.player_state = 5.5
                self.contador = 0

    def strongKick(self):
        if self.direcao == 1:
            if self.player_state != 6:
                self.player.set_sequence(60, 68)
                self.player.set_curr_frame(60)
                self.player_state = 6
                self.contador = 0
        elif self.direcao == 2:
            if self.player_state != 6.5:
                self.player.set_sequence(68, 76)
                self.player.set_curr_frame(68)
                self.player_state = 6.5
                self.contador = 0


    def checarContador(self):
        if self.player_state == 3 or self.player_state == 3.5:
            return 1.4
        elif self.player_state == 4 or self.player_state == 4.5:
            return 1.4
        elif self.player_state == 5 or self.player_state == 5.5:
            return 1.9
        elif self.player_state == 6 or self.player_state == 6.5:
            return 1.9        
        else: return 0

    def run(self):
        
        tempoContador = self.checarContador()

        if self.contador >= tempoContador:
            # I - Soco forte / L - Chute Duplo / J - Soco fraco / K - Chute normal
            if(self.teclado.key_pressed("J")):
                self.weakPunch()
            elif(self.teclado.key_pressed("L")):
                self.weakKick()
            elif(self.teclado.key_pressed("K")):
                self.strongPunch()
            elif(self.teclado.key_pressed("I")):
                self.strongKick()

            #Movimentação Básica
            elif(self.teclado.key_pressed("D") and self.teclado.key_pressed("W")):
                self.walkRightUp()
            elif(self.teclado.key_pressed("D") and self.teclado.key_pressed("S")):
                self.walkRightDown()
            elif(self.teclado.key_pressed("D")):
                self.walkRight()
            elif(self.teclado.key_pressed("A") and self.teclado.key_pressed("W")):
                self.walkLeftUp()
            elif(self.teclado.key_pressed("A") and self.teclado.key_pressed("S")):
                self.walkLeftDown()
            elif(self.teclado.key_pressed("A")):
                self.walkLeft()
            elif(self.teclado.key_pressed("W")):
                self.walkUp()
            elif(self.teclado.key_pressed("S")):
                self.walkDown()
            else:
                if self.direcao == 1:
                    self.idleRight()
                elif self.direcao == 2:
                    self.idleLeft()


        self.contador += self.janela.delta_time()
        self.player.draw()
        self.player.play()
        self.player.update()
        self.contador += self.janela.delta_time()
