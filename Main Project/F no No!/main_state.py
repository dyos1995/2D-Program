import random
import os

from pico2d import *

import game_framework
import title_state
import papera_state
import paperb_state
import paperc_state
import paperf_state

from boy import Boy
from grass import Grass
from Fall import FallF
from Fall import FallC
from Fall import FallB
from Fall import FallA
from grade import Grade

name = "MainState"
image = None
boy = None
grass = None
fallf = None
grade = None
font = None
running = None
judge = 0
counter = 0
Fcount = 0
timer = 0.0
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
            boy.handle_event(event,frame_time)


def create_world():
    global boy, grass, fallf, grade
    boy = Boy()
    grass = Grass()
    grade = Grade()
    fallf = []


def enter():
    global image
    global font
    global timer
    timer = 0.0
    image = load_image('main_picture.png')
    font = load_font('ENCR10B.TTF', 30)
    game_framework.reset_time()
    create_world()



def exit():
    global boy, grass, fallf, grade
    global image
    del(image)
    del(boy)
    del(fallf)
    del(grass)
    del(grade)

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
   global timer
   global boy, grade, fallf, grass
   frand = random.randint(1, 10)
   crand = random.randint(1, 10)
   krand = random.randint(1, 3)
   counter += 1
   timer += 0.01

   boy.update(frame_time)
   grade.update(frame_time)

   if counter % 7 == 0:
       Fcount += 1
       if frand == 3:
           fallf.append(FallB())
       if timer > 30:
           if krand == 2:
               fallf.append(FallC())
           if timer > 60:
               if frand == 3:
                   fallf.append(FallB())
               if timer > 90:
                   if crand == 3:
                       fallf.append(FallA())

# 시간 초별 다른 결과 값
   for fallfs in fallf:
       fallfs.update(frame_time)
       if fallfs.dir == 5:
           fallf.remove(fallfs)

       if collide(boy, fallfs):
           if timer > 0 and timer < 30:
               game_framework.push_state(paperf_state)
           if timer > 30 and timer < 60:
               game_framework.push_state(paperc_state)
           if timer > 60 and timer < 90:
               game_framework.push_state(paperb_state)
           if timer > 90 and timer < 120:
               game_framework.push_state(papera_state)
# 땅에 충돌시 fallf의 리스트내 fallf 삭제
       if collide(grass, fallfs):
            fallf.remove(fallfs)




# 그리기 함수
def draw(frame_time):
    global boy, grade, fallf, grass
    global timer
    clear_canvas()
    image.draw(400, 300)
    grass.draw()
    boy.draw(frame_time)
    grade.draw()
    #수정됨 1
    font.draw(370, 550, '%3.2f' % timer, (0, 120, 125))

    #떨어지는 장애물 떨어지는 코드
    for fallfs in fallf:
        fallfs.draw()

    # 충돌 경계선 그리기
    grass.draw_bb()
    boy.draw_bb()

    for fallfs in fallf:
        fallfs.draw_bb()
    update_canvas()

#메인 함수
def main():
    global running
    global frame_time

    enter()
    running = True

    while running:
        handle_events(frame_time)
        update(frame_time)

        draw()

    exit()


if __name__ == '__main__':
    main()

