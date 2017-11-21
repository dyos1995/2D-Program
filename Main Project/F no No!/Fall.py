import random
import main_state
from pico2d import *

class FallF():
    image = None

    def __init__(self):
        self.x, self.y = random.randint(0, 800), 600
        self.RUN_SPEED_KMPH = random.randint(10, 30)
        self.dir = 1
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

#B 학점 떨어지기
class FallB():
    image = None

    def __init__(self):
        self.x, self.y = 0.0, 0.0
        self.x1, self.y1 = random.randint(0, 800), random.randint(300, 600)
        self.RUN_SPEED_KMPH = 2
        self.dir = 1
        self.pie = 3.141592 / 180
        self.rad = 0
        self.cicle = 0.0
        if FallB.image == None:
            FallB.image = load_image('Fall grade B.png')


    def update(self, frame_time):
        PIXEL_PER_METER = (10.0 / 0.3)
        RUN_SPEED_MPM = (self.RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.fall_speed = RUN_SPEED_PPS * frame_time
        self.cicle += self.fall_speed
        self.rad += 2
        self.x = self.cicle * math.cos(self.rad* self.pie) + self.x1
        self.y = self.cicle * math.sin(self.rad* self.pie) + self.y1


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

#A 학점 떨어지기
class FallA():
    image = None
    def __init__(self):
        self.x, self.y = random.randint(0, 800), random.randint(0, 300)
        self.RUN_SPEED_KMPH = 5
        self.dir = 1
        self.speed = 0.0
        self.timer = 0.0
        if FallA.image == None:
            FallA.image = load_image('Fall grade A.png')

    def update(self, frame_time):
        self.speed += frame_time
        if self.speed > 0.5:
            self.dir = 5

    def draw(self):
        self.image.draw(self.x, self.y)

    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())