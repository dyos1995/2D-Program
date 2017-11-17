import random
import os

from pico2d import *

import game_framework
import title_state
from boy import Boy
from grass import Grass
from Fall import FallF
from Fall import FallC
from grade import Grade
from grade import Paper

name = "MainState"
image = None
boy = None
grass = None
fallf = None
grade = None
font = None
running = None
paper = None
judge = 0
counter = 0;
Fcount = 0;
current_time = 0.0

def handle_events(frame_time):
    global running
    global boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            else:
                boy.handle_event(event,frame_time)


def create_world():
    global boy, grass, fallf, grade, paper
    boy = Boy()
    grass = Grass()
    grade = Grade()
    paper = Paper()
    fallf = []


def enter():
    global image
    image = load_image('main_picture.png')
    game_framework.reset_time()
    create_world()



def exit():
    global boy, grass, fallf,grade, paper
    global image
    del(image)
    del(boy)
    del(fallf)
    del(grass)
    del(grade)
    del(paper)

def pause():
    pass


def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

# 업데이트
def update(frame_time):
   global counter
   global Fcount
   counter += 1
   boy.update(frame_time)
   grade.update(frame_time)

   if counter % 10 == 0:
       Fcount += 1
       fallf.append(FallF())
       if get_time() > 30:
           fallf.append(FallC())

   for fallfs in fallf:
       fallfs.update(frame_time)
       if collide(boy, fallfs):
           fallf.remove(fallfs)
       if collide(grass, fallfs):
            fallf.remove(fallfs)




# 그리기 함수
def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    grass.draw()
    boy.draw()
    grade.draw()
    for fallfs in fallf:
        fallfs.draw()
    grass.draw_bb()
    boy.draw_bb()

    for fallfs in fallf:
        fallfs.draw_bb()
    update_canvas()


def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


#메인 함수
def main():
    global running
    global current_time


    enter()
    running = True
    current_time = get_time()

    while running:
        frame_time = get_frame_time()
        handle_events(frame_time)
        update(frame_time)

        draw()
        get_frame_time()

    exit()


if __name__ == '__main__':
    main()

