import random
import main_state
from pico2d import *

# 실드
class DeadEffection():
    image = None

    def __init__(self):
        self.x, self.y = main_state.boy.x , main_state.boy.y
        self.RUN_SPEED_KMPH = random.randint(20, 30)
        self.judge = 0
        self.frame = 0
        self.state = 0
        self.timer1 = 0.0
        if DeadEffection.image == None:
            DeadEffection.image = load_image('blood.png')

    def update(self, frame_time):
        self.x = main_state.boy.x
        self.y = main_state.boy.y

    def draw(self):
        self.image.draw(400, 300)
