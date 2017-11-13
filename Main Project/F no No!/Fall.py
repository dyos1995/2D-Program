import random
from pico2d import *

class FallF():
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.fall_speed = random.randint(50,120)
        if FallF.image == None:
            FallF.image = load_image('ball21x21.png')

    def update(self, frame_time):
        self.y -= frame_time * self.fall_speed
        if self.y < 60:
            self.fall_speed = 0
            self.y = 70


    def draw(self):
        self.image.draw(self.x, self.y)

    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return self.x - 8, self.y - 8, self.x + 8, self.y + 8

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

