from pico2d import *
import random

class Grass:
    def __init__(self):
        self.x = 400
        self.y = 30
        self.image = load_image('grass.png')
        self.bgm = load_music('load_main_sound.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400, 30)

    def get_bb(self):
        return self.x - 400, self.y - 30, self.x + 400, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

