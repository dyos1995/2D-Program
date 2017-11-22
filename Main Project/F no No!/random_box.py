import random
import main_state
from pico2d import *

class RandB():
    image = None

    def __init__(self):
        self.x, self.y = random.randint(0, 800), 600
        self.RUN_SPEED_KMPH = random.randint(20, 30)
        self.dir = random.randint(1, 2)
        if RandB.image == None:
            RandB.image = load_image('random_box.png')


    def update(self, frame_time):
        PIXEL_PER_METER = (10.0 / 0.3)
        RUN_SPEED_MPM = (self.RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.fall_speed = RUN_SPEED_PPS * frame_time
        self.y -= self.fall_speed


    def draw(self):
        self.image.draw(self.x, self.y)

    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return self.x - 13, self.y - 13, self.x + 13 , self.y + 13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Cloud():
    image = None

    def __init__(self):
        self.x, self.y = 400, 300
        self.RUN_SPEED_KMPH = random.randint(20, 30)
        self.dir = random.randint(1, 2)
        self.judge = 0
        self.timer1 = 0.0
        if Cloud.image == None:
            Cloud.image = load_image('cloud.png')


    def update(self, frame_time):
        if self.judge == 1:
            print("%f" %self.timer1)
            self.timer1 += frame_time
            if self.timer1 > 1.0:
                self.judge = 0


    def draw(self):
        self.image.draw(self.x, self.y)

    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

# 실드
class Shield():
    image = None

    def __init__(self):
        self.x, self.y = main_state.boy.x , main_state.boy.y
        self.RUN_SPEED_KMPH = random.randint(20, 30)
        self.dir = random.randint(1, 2)
        self.judge = 0
        self.timer1 = 0.0
        if Shield.image == None:
            Shield.image = load_image('ShieldB.png')


    def update(self, frame_time):
        self.x = main_state.boy.x
        self.y = main_state.boy.y
        if main_state.timer3 < 1:
            Shield.image = load_image('shieldB.png')
        if main_state.timer3 > 1 and main_state.timer3 < 2:
            Shield.image = load_image('shieldG.png')
        if main_state.timer3 > 2 and main_state.timer3 < 3:
            Shield.image = load_image('shieldW.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return self.x - 95, self.y - 95, self.x + 95, self.y + 95

    def draw_bb(self):
        draw_rectangle(*self.get_bb())