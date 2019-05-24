class GameController:
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.pos = list()
        for x in range(1, size+1):
            self.pos.append((((x*width/size)+((x-1)*width/size))/2))
