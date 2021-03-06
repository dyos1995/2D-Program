import random
import json
from pico2d import *

class Boy:
    image = None
    font = None
    hit_sound = None
    make_shield = None
    make_cloud = None
    fired = None

    global judge

    #10픽셀당 3m
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    LEFT_HIT, RIGHT_HIT, LEFT_JUMP, RIGHT_JUMP, LEFT_STAND, RIGHT_STAND, LEFT_RUN,  RIGHT_RUN = 0, 1, 2, 3, 4, 5, 6, 7,

    #키 입력에 관한 BOY의 행동
    def handle_event(self, event, frame_time):
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
        elif(event.type, event.key) ==(SDL_KEYDOWN, SDLK_SPACE):
            if self.jump_frames == 0:
                self.jump_frames = 1


    #핸들 이벤트의 이동
    def handle_left_run(self,frame_time):
        self.dir = -1

    def handle_left_stand(self,frame_time):
        self.stand_frames += 1

    def handle_right_run(self,frame_time):
        self.dir = 1

    def handle_right_stand(self,frame_time):
        self.stand_frames += 1

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
    }

    def update(self, frame_time):
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.x += (self.dir * distance)

        if self.state >= 6:
            self.frame = int(self.total_frames + 1) % 6
        else:
            self.frame = int(self.total_frames + 1) % 2

        # jump frame
        if self.jump_frames == 1:
            self.y += distance*2
            self.jump += 1
            if self.jump > 10:
                self.jump_frames = 2

        if self.jump_frames == 2:
            self.y -= distance *2
            self.jump -= 1
            if self.jump < 0:
                self.jump_frames = 0
                self.y = 90

        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 5)

        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x - 5)


    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 6)
        self.stand_frames = 0
        self.jump_frames = 0
        self.jump = 0
        self.total_frames = 0.0
        self.dir = 0
        self.state = self.RIGHT_STAND
        self.name = 'noname'
        if Boy.image == None:
            Boy.image = load_image('run_animation.png')
        if Boy.hit_sound == None:
            Boy.hit_sound = load_wav('touch.wav')
            Boy.hit_sound.set_volume(50)
        if Boy.make_shield == None:
            Boy.make_shield = load_wav('shieldSound.wav')
            Boy.make_shield.set_volume(100)
        if Boy.make_cloud == None:
            Boy.make_cloud = load_wav('makecloud.wav')
            Boy.make_cloud.set_volume(100)
        if Boy.fired == None:
            Boy.fired = load_wav('yourfired.wav')
            Boy.fired.set_volume(100)

    def hit(self, ball):
        self.hit_sound.play()

    def fire_hit(self):
        self.fired.play()

    def shield_hit(self):
        self.make_shield.play()

    def cloud_hit(self):
        self.make_cloud.play()

    #충돌 체크 사각형 생성
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 45

    def draw(self,frame_time):
        self.image.clip_draw(self.frame * 50, self.state * 100, 50, 100, self.x, self.y)
