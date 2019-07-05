from PPlay.sound import Sound
class Sound_controller():
    def __init__(self):
        self.tema = Sound("assets/theme.ogg")
        self.gameover = Sound("assets/game_over.ogg")
        self.tema.set_volume(10)
        self.gameover.set_volume(20)

    def run(self):
        self.tema.play()