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
from Falls import FallF
from Falls import FallC
from Falls import FallB
from Falls import FallA
from grade import Grade
from random_boxs import RandB
from random_boxs import Cloud
from random_boxs import Shield

name = "MainState"
image = None
boy = None
grass = None
fallf = None
grade = None
font = None
running = None
randb = None
cloud = None
shield = None
judge1 = 0
judge2 = 0
counter = 0
Fcount = 0
timer = 0.0
timer2 = 0.0
timer3 = 0.0
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
    global boy, grass, fallf, grade, randb, cloud, shield
    boy = Boy()
    randb = []
    shield = Shield()
    grass = Grass()
    grade = Grade()
    cloud = Cloud()
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
    global boy, grass, fallf, grade, randb, cloud, shield
    global image
    del(image)
    del(shield)
    del(randb)
    del(boy)
    del(fallf)
    del(grass)
    del(grade)
    del(cloud)

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
   global timer, timer2, timer3
   global judge1, judge2
   global boy, grade, fallf, grass
   frand = random.randint(1, 100)
   crand = random.randint(1, 40)
   krand = random.randint(1, 200)
   counter += 1
   timer += 0.01

   boy.update(frame_time)
   grade.update(frame_time)
   cloud.update(frame_time)
   shield.update(frame_time)
   if krand == 3:
       randb.append(RandB())

   # 0 ~ 20초 까지 속도
   if timer > 0 and timer < 20:
       if counter % 6 == 0:
           Fcount += 1
           fallf.append(FallF())

   # 20 ~ 40초 까지 속도
   if timer > 20 and timer < 40:
       if counter % 10 == 0:
           fallf.append(FallF())
       if counter % 14 == 0:
           fallf.append(FallC())

   # 20 ~ 40초 까지 속도
   if timer > 40 and timer < 60:
       if counter % 20 == 0:
           fallf.append(FallF())
       if counter % 25 == 0:
           fallf.append(FallC())
       if frand == 3:
           fallf.append(FallB())

   # 40 ~ 60초 까지 속도
   if timer > 60 and timer < 80:
       if counter % 20 == 0:
           fallf.append(FallF())
       if counter % 25 == 0:
           fallf.append(FallC())
       if frand == 3:
           fallf.append(FallB())
       if crand == 3:
           fallf.append(FallA())

# 랜덤 박스 ~~~~~~~~~~~~
   if judge1 == 1:
       timer2 += 0.01
   if judge2 == 1:
       timer3 += 0.01


   for randbs in randb:
       randbs.update(frame_time)
       if collide(grass, randbs):
           randb.remove(randbs)
       if collide(boy, randbs):
           print("%d"  %randbs.dir)
           # 구름
           if randbs.dir == 1:
               judge1 = 1
           # 무적도
           if randbs.dir == 2:
               judge2 = 1
           randb.remove(randbs)




# 시간 초별 다른 결과 값 / F가 떨어진다네
   for fallfs in fallf:
       fallfs.update(frame_time)
       if fallfs.dir == 5:
           fallf.remove(fallfs)

       if collide(boy, fallfs):
           boy.hit(fallfs)
           if timer > 0 and timer < 20:
               game_framework.push_state(paperf_state)
           if timer > 20 and timer < 40:
               game_framework.push_state(paperc_state)
           if timer > 40 and timer < 60:
               game_framework.push_state(paperb_state)
           if timer > 60 and timer < 80:
               game_framework.push_state(papera_state)

# 땅에 충돌시 fallf의 리스트내 fallf 삭제
       if collide(grass, fallfs):
            fallf.remove(fallfs)
       if judge2 == 1:
           if collide(shield, fallfs):
               fallf.remove(fallfs)



# 그리기 함수
def draw(frame_time):
    global boy, grade, fallf, grass, randb
    global timer, timer2, timer3
    global judge1, judge2

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
    for randbs in randb:
        randbs.draw()
    # 충돌 경계선 그리기
#    grass.draw_bb()
#    boy.draw_bb()

#    for fallfs in fallf:
#        fallfs.draw_bb()

#    for randbs in randb:
#        randbs.draw_bb()

# 구름 등장!!!!
    if judge1 == 1:
        cloud.draw()
        if timer2 > 3.0:
            judge1 = 0
            timer2 = 0.0

    if judge2 == 1:
        shield.draw()
 #       shield.draw_bb()
        if timer3 > 5.0:
            judge2 = 0
            timer3 = 0.0

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

