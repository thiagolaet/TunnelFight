class Food():
    def __init__(self, sprite, heal):
        self.sprite = sprite
        self.timer = 0
        self.heal = heal

    def update(self):
        self.sprite.update()