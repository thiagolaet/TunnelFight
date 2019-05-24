class Nave(object):
    def __init__(self, position_max, sprite, jan_w, gc):
        self.position = 1
        self.position_max = 2 #position vai de 0 a position_max
        self.sprite = sprite
        self.jan_w = jan_w
        self.game_controller = gc

    def getPosition(self):
        return self.position

    def setPosition(self, direction):
        if direction == "+":
            self.position = self.position + 1
            if self.position > self.position_max:
                self.position = 0
        elif direction == "-":
            self.position = self.position - 1
            if self.position < 0:
                self.position = self.position_max
        self.position_nave()

    def position_nave(self):
        self.sprite.x = self.game_controller.pos[self.position] - (self.sprite.width/2)

    def update(self):
        self.sprite.draw()