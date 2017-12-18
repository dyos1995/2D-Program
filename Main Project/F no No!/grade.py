import random
import main_state
from pico2d import *

class Grade():
    image = None

    def __init__(self):
        self.x, self.y = 770, 570


    def update(self, frame_time):
        # 수정됨 1
        if main_state.timer > 0 and main_state.timer < 10:
            Grade.image = load_image('GradeF.png')
        elif main_state.timer > 10 and main_state.timer < 20:
            Grade.image = load_image("GradeC.png")
        elif main_state.timer > 20 and main_state.timer < 30:
            Grade.image = load_image("GradeB.png")
        elif main_state.timer > 30 and main_state.timer < 40:
            Grade.image = load_image("GradeA.png")

    def draw(self):
        self.image.opacify(0.7)
        self.image.draw(self.x, self.y)

