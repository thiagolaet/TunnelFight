class Life():
    def __init__(self):
        self.maxLife = 100
        self.currentLife = 100
        self.alive = True

    def receive_damage(self, damage):
        self.currentLife -= damage
        if self.currentLife < 0:
            self.currentLife = 0
            self.alive = False
            return

    def reset_life(self):
        self.currentLife = self.maxLife
