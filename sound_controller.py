from PPlay.sound import Sound
class Sound_controller():
    def __init__(self):
        self.tema = Sound("assets/theme.ogg")
        self.tema.set_volume(10)

    def run(self):
        self.tema.play()