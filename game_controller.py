from random import sample
from random import randrange
from PPlay.sprite import Sprite
from time import time
class GameController:
    def __init__(self, strt, player, enemycontroller, janela):
        self.player = player
        self.enemy_controller = enemycontroller
        self.start_enemies = strt
        self.current_wave = 1
        self.wave_time_counter = 0
        self.janela = janela
        self.food_list = []


    def wave_controller(self):
        if len(self.enemy_controller.enemyList) == 0:
            self.wave_time_counter += self.janela.delta_time()
            if self.wave_time_counter >= 2: 
                self.wave_time_counter = 0
                self.enemy_controller.start_a_wave(self.start_enemies + self.current_wave)
                self.spawn_food()
                print("Wave: " + str(self.current_wave))
                self.current_wave += 1

    def spawn_food(self):
        index = randrange(0, 3)
        if index == 0:
            food = Sprite("assets/frango_assado.png")
        elif index == 1:
            food = Sprite("assets/taco.png")
        elif index == 2:
            food = Sprite("assets/sushi.png")
        food.x = randrange(0, self.janela.width - food.width)
        food.y = randrange(self.janela.height/2, self.janela.height)

        self.food_list.append(food)


    def player_enemy_list(self):
        temp = []
        temp2 = []
        for a in self.enemy_controller.enemyList:
            if a.enemy.collided(self.player.player):
                temp.append(a)
        if len(temp) > 0:
            n = 3 if len(temp) >= 3 else len(temp)
            temp2 = sample(range(len(temp)), n)
            for a in range(0, len(temp2)):
                temp2[a] = temp[temp2[a]]
        self.player.enemy_list = temp2


    def draw(self):
        templist = []
        templist.append(self.player.player)
        for a in self.food_list:
            templist.append(a)
        templist.extend(self.enemy_controller.dieList)
        for a in self.enemy_controller.enemyList:
            templist.append(a.enemy)
        def swap(i, j):
            templist[i], templist[j] = templist[j], templist[i]
        n = len(templist)
        swapped = True
        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n - x):
                if templist[i - 1].y + templist[i - 1].width > templist[i].y + templist[i].width:
                    swap(i - 1, i)
                    swapped = True

        for a in range(len(templist)):
            templist[a].draw()

    def run(self):
        self.wave_controller()
        self.player_enemy_list()

        self.draw()
