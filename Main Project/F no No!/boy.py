import random

from pico2d import *

class Boy:
    image = None
    global judge

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
        self.plus += 1
        if(self.plus % 10 == 0):
            self.run_frames += 1


    def handle_left_stand(self):
        self.stand_frames += 1

    def handle_right_run(self):
        self.dir = 1
        self.plus += 1
        if(self.plus % 10 == 0):
            self.run_frames += 1

    def handle_right_stand(self):
        self.stand_frames += 1

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }

    def update(self, frame_time):
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
        self.frame = random.randint(0, 6)
        self.stand_frames = 0
        self.total_frames = 0.0
        self.plus = 0
        self.dir = 0
        self.state = self.RIGHT_STAND
        self.name = 'noname'
        if Boy.image == None:
            Boy.image = load_image('run_animation.png')

    #충돌 체크 사각형 생성
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 45

    def draw(self):
        #self.image.clip_draw(self.frame * 25, self.state * 50, 25, 50, self.x, self.y)