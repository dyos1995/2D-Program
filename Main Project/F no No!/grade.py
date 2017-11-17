import random
from pico2d import *

class Grade():
    image = None

    def __init__(self):
        self.x, self.y = 770, 570
        if Grade.image == None:
            Grade.image = load_image('GradeF.png')


    def update(self, frame_time):
        if(get_time() > 30 and get_time() < 60):
            Grade.image = load_image("GradeC.png")
        elif get_time() > 60 and get_time() < 90:
            Grade.image = load_image("GradeB.png")
        elif get_time() > 90 and get_time() < 120:
            Grade.image = load_image("GradeA.png")

    def draw(self):
        self.image.opacify(0.7)
        self.image.draw(self.x, self.y)

class Paper():
    image = None

    def __init__(self):
        self.x, self.y = 400, 300
        if Grade.image == None:
            Grade.image = load_image('PaperF.png')


    def update(self, frame_time):
        if(get_time() > 30 and get_time() < 60):
            Grade.image = load_image("PaperC.png")
        elif get_time() > 60 and get_time() < 90:
            Grade.image = load_image("PaperB.png")
        elif get_time() > 90 and get_time() < 120:
            Grade.image = load_image("PaperA.png")

    def draw(self):
        self.image.draw(self.x, self.y)
