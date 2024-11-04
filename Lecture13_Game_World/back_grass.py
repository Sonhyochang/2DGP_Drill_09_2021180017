from pico2d import load_image

class Back_Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 50)

    def update(self):
        pass