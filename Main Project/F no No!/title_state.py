import game_framework
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del(image)


def handle_events():
    pass


def draw():
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






