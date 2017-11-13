import random
import os

from pico2d import *

import game_framework
import title_state
from boy import Boy
from grass import Grass
from Fall import FallF


name = "MainState"
image = None
boy = None
grass = None
fallf = None
font = None
judge = 0
running = None

def handle_events(frame_time):
    global running
    global boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif(event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            else:
                boy.handle_event(event)

def create_world():
    global boy, grass,fallf
    boy = Boy()
    grass = Grass()
    fallf = [FallF() for i in range(10)]

def enter():
    global image
    image = load_image('main_picture.png')
    game_framework.reset_time()
    create_world()




def exit():
    global boy, grass, fallf
    global image
    del(image)
    del(boy)
    del(fallf)
    del(grass)


def pause():
    pass


def resume():
    pass


# 업데이트
def update(frame_time):
   boy.update(frame_time)
   for fallfs in fallf:
       fallfs.update(frame_time)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


# 그리기 함수
def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    grass.draw()
    boy.draw()
    for fallfs in fallf:
        fallfs.draw()
    grass.draw_bb()
    boy.draw_bb()
    for fallfs in fallf:
        fallfs.draw_bb()
    update_canvas()




#메인 함수
def main():
    global running
    global current_time
    global frame_rate
    enter()
    running = True
    current_time = get_time()

    while running:
        handle_events()
        update()
        draw()

    exit()


if __name__ == '__main__':
    main()

