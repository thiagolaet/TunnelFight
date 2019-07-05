from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
import globals
from life import*

class Player():
    def __init__(self, janela):
        self.janela = janela
        self.teclado = janela.get_keyboard()

        self.player = Animation("assets/player-animation-2.png", 77)
        self.player.set_position(self.janela.width/2 - self.player.width/2, 360)
        self._set_seq_time()
        
        self.attack_rate = 0

        #1 = direita / 2 = esquerda
        self.direcao = 1

        #1 - idleRight / 1.5 - idleLeft / 2 - walkRight / 2.5 - walkLeft / 3 3.5 - attack1 / 4 4.5 - attack2 / 5 5.5 - attack3 / 6 6.5 - attack4  
        self.player_state = 1
        self.contadorAnimacao = 0
        self.player.set_sequence(0, 4)

        #sistema de vida
        self.life = Life()

        #inimgos que tomarão dano no próximo ataque
        self.enemy_list = []

        self.hitbox = Sprite("assets/hitbox_player.png")


    def _set_seq_time(self):
        self.player.set_sequence_time(0, 4, 130)    
        self.player.set_sequence_time(4, 8, 130)
        self.player.set_sequence_time(8, 16, 100)
        self.player.set_sequence_time(16, 24, 100)
        self.player.set_sequence_time(24, 28, 120)
        self.player.set_sequence_time(28, 32, 120)
        self.player.set_sequence_time(32, 37, 120)
        self.player.set_sequence_time(37, 42, 120)
        self.player.set_sequence_time(42, 50, 100)
        self.player.set_sequence_time(50, 58, 100)
        self.player.set_sequence_time(59, 61, 120)
        self.player.set_sequence_time(61, 64, 120)
        self.player.set_sequence_time(64, 70, 150)
        self.player.set_sequence_time(70, 77, 150)


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
        self.player.x += 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 1

    def walkRightUp(self):
        if self.player_state != 2: 
            self.player.set_sequence(8, 16)
            self.player_state = 2
        self.player.y -= self.janela.delta_time() * globals.frame_per_SECOND 
        self.player.x += 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 1

    def walkRightDown(self):
        if self.player_state != 2: 
            self.player.set_sequence(8, 16)
            self.player_state = 2
        self.player.y += self.janela.delta_time() * globals.frame_per_SECOND 
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
        self.player.y -= self.janela.delta_time() * globals.frame_per_SECOND 
        self.player.x -= 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 2

    def walkLeftDown(self):
        if self.player_state != 2.5:
            self.player.set_sequence(16, 24)
            self.player_state = 2.5
        self.player.y += self.janela.delta_time() * globals.frame_per_SECOND 
        self.player.x -= 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 2

    def walkUp(self):
        if self.direcao == 1:
            self.player.y -= self.janela.delta_time() * globals.frame_per_SECOND 
            if self.player_state != 2: 
                self.player.set_sequence(8, 16)
                self.player_state = 2
        if self.direcao == 2:
            self.player.y -= self.janela.delta_time() * globals.frame_per_SECOND 
            if self.player_state != 2.5: 
                self.player.set_sequence(16, 24)
                self.player_state = 2.5

    def walkDown(self):
        if self.direcao == 1:
            self.player.y += self.janela.delta_time() * globals.frame_per_SECOND 
            if self.player_state != 2: 
                self.player.set_sequence(8, 16)
                self.player_state = 2
        if self.direcao == 2:
            self.player.y += self.janela.delta_time() * globals.frame_per_SECOND 
            if self.player_state != 2.5: 
                self.player.set_sequence(16, 24)
                self.player_state = 2.5

    def weakPunch(self):
        if self.attack_rate <= 0:
            self.attack_rate = 0.5
            if self.direcao == 1:
                if self.player_state != 3:
                    self.player.set_sequence(24, 28)
                    self.player.set_curr_frame(24)
                    self.player_state = 3
                    self.contadorAnimacao = 0
            elif self.direcao == 2:
                if self.player_state != 3.5:
                    self.player.set_sequence(28, 32)
                    self.player.set_curr_frame(28)
                    self.player_state = 3.5
                    self.contadorAnimacao = 0

            for a in self.enemy_list:
                if not a.atacando and ((a.enemy.x < self.player.x and self.direcao == 2) or (a.enemy.x  > self.player.x and self.direcao == 1)):
                    if self.player.y < a.enemy.y and self.player.y + self.player.height > a.enemy.y + a.enemy.height:
                        a.life.receive_damage(10)
                        a.tomouDano = True


    def weakKick(self):
        if self.attack_rate <= 0:
            self.attack_rate = 0.7
            if self.direcao == 1:
                if self.player_state != 4:
                    self.player.set_sequence(32, 37)
                    self.player.set_curr_frame(32)
                    self.player_state = 4
                    self.contadorAnimacao = 0
            elif self.direcao == 2:
                if self.player_state != 4.5:
                    self.player.set_sequence(37, 42)
                    self.player.set_curr_frame(37)
                    self.player_state = 4.5
                    self.contadorAnimacao = 0
            for a in self.enemy_list:
                if not a.atacando and ((a.enemy.x  < self.player.x and self.direcao == 2) or (a.enemy.x  > self.player.x and self.direcao == 1)):
                    if self.player.y < a.enemy.y and self.player.y + self.player.height > a.enemy.y + a.enemy.height:
                        a.life.receive_damage(20)
                        a.tomouDano = True

    def strongKick(self):
        if self.attack_rate <= 0:
            self.attack_rate = 1.2
            if self.direcao == 1:
                if self.player_state != 6:
                    self.player.set_sequence(42, 50)
                    self.player.set_curr_frame(42)
                    self.player_state = 5
                    self.contadorAnimacao = 0
            elif self.direcao == 2:
                if self.player_state != 6.5:
                    self.player.set_sequence(50, 58)
                    self.player.set_curr_frame(50)
                    self.player_state = 5.5
                    self.contadorAnimacao = 0
            for a in self.enemy_list:
                if not a.atacando and ((a.enemy.x  < self.player.x and self.direcao == 2) or (a.enemy.x  > self.player.x and self.direcao == 1)):
                    if self.player.y < a.enemy.y and self.player.y + self.player.height > a.enemy.y + a.enemy.height:
                        a.life.receive_damage(30)
                        a.tomouDano = True


    def checarcontadorAnimacao(self):
        if self.player_state == 3 or self.player_state == 3.5:
            return 0.4
        elif self.player_state == 4 or self.player_state == 4.5:
            return 0.5
        elif self.player_state == 5 or self.player_state == 5.5:
            return 0.8
        else: return 0

    def checarLimiteMapa(self):
        if self.player.y < 278:
            self.player.y = 278

        if self.player.x + 45 < 0:
            self.player.x = -45

        if self.player.x + self.player.width - 45 > self.janela.width:
            self.player.x = self.janela.width - self.player.width + 45

        if self.player.y + self.player.height - 30 > 600:
            self.player.y = 600 + 30 - self.player.height

    def run(self):
        
        self.checarLimiteMapa()
        self.hitbox.set_position(self.player.x + 48, self.player.y + 36)
        tempocontadorAnimacao = self.checarcontadorAnimacao()

        if self.contadorAnimacao >= tempocontadorAnimacao:
            

            #Movimentação Básica
            if(self.teclado.key_pressed("D") and self.teclado.key_pressed("W")):
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

            #K - Chute Duplo / J - Soco fraco / K - Chute normal
            if self.attack_rate <= 0:
                if(self.teclado.key_pressed("J")):
                    self.weakPunch()
                elif(self.teclado.key_pressed("L")):
                    self.weakKick()
                elif(self.teclado.key_pressed("K")):
                    self.strongKick()

        self.attack_rate -= self.janela.delta_time()
        #self.player.draw()
        self.player.play()
        self.player.update()
        self.contadorAnimacao += self.janela.delta_time()
