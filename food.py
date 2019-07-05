from PPlay.animation import Animation
class Food():
    def __init__(self, sprite, heal):

        self.sprite = sprite
        self.sprite.set_sequence_time(0, 4, 200)
        self.timer = 0
        self.heal = heal

    def update(self):
        self.sprite.update()