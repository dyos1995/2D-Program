import random
from pico2d import *

class FallF():
    image = None



    def __init__(self):
        self.x, self.y = random.randint(0, 800), 600
        self.RUN_SPEED_KMPH = random.randint(5, 20)
        if FallF.image == None:
            FallF.image = load_image('Fall grade F.png')


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
        return self.x - 10, self.y - 10, self.x + 10, self.y + 13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class FallC():
    image = None



    def __init__(self):
        self.x, self.y = random.randint(0, 800), 600
        self.RUN_SPEED_KMPH = random.randint(5, 20)
        self.dir = random.randint(1, 2)
        if FallC.image == None:
            FallC.image = load_image('Fall grade C.png')


    def update(self, frame_time):
        PIXEL_PER_METER = (10.0 / 0.3)
        RUN_SPEED_MPM = (self.RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.fall_speed = RUN_SPEED_PPS * frame_time
        if self.dir == 1:
            self.y -= self.fall_speed
            self.x -= self.fall_speed
        elif self.dir == 2:
            self.y -= self.fall_speed
            self.x += self.fall_speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

