import random
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"
image = None
boy = None
grass = None
font = None
judge = 0
running = None
frame_time = 0
frame_rate = 0

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    image = None
    global judge
    global frame_time
    global frame_rate

    #10픽셀당 3m
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8


    LEFT_HIT, RIGHT_HIT, LEFT_JUMP, RIGHT_JUMP, LEFT_STAND, RIGHT_STAND, LEFT_RUN,  RIGHT_RUN = 0, 1, 2, 3, 4, 5, 6, 7,

    #키 입력에 관한 BOY의 행동
    def handle_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN
            elif self.state in (self.RIGHT_RUN, ):
                self.state = self.LEFT_RUN
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_RUN
            elif self.state in (self.LEFT_RUN,):
                self.state = self.RIGHT_RUN
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN, ):
                self.state = self.LEFT_STAND
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN, ):
                self.state = self.RIGHT_STAND

    #핸들 이벤트의 이동
    def handle_left_run(self):
        self.dir = -1
        self.run_frames += 1


    def handle_left_stand(self):
        self.stand_frames += 1

    def handle_right_run(self):
        self.dir = 1
        self.run_frames += 1

    def handle_right_stand(self):
        self.stand_frames += 1

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def update(self):
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.x += (self.dir * distance)

        if(self.state >= 7):
            self.frame = (self.frame + 1) % 6
        else:
            self.frame = (self.frame + 1) % 2

        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x - 5)

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 5)
        self.stand_frames = 0
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.RIGHT_STAND
        self.name = 'noname'
        if Boy.image == None:
            Boy.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 50, self.state * 100, 50, 100, self.x, self.y)


def handle_events():
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


def enter():
    global boy
    global grass
    global image
    image = load_image('main_picture.png')
    boy = Boy()
    grass = Grass()


def exit():
    global boy, grass
    global image
    del(image)
    del(boy)
    del(grass)


def pause():
    pass


def resume():
    pass


# 업데이트
def update():
   boy.update()


# 그리기 함수
def draw():
    clear_canvas()
    image.draw(400, 300)
    grass.draw()
    boy.draw()
    update_canvas()




#메인 함수
def main():
    global running
    global current_time
    global frame_time
    global frame_rate
    enter()
    running = True
    current_time = get_time()

    while running:
        handle_events()
        update()
        draw()

        frame_time = get_time() - current_time
        frame_rate = 1.0 / frame_time
        current_time += frame_time
    exit()


if __name__ == '__main__':
    main()

