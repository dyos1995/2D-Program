import game_framework
from pico2d import *

import main_state


name = "Pause"
image1 = None
boy = None
grass = None
fallf = None
grade = None
font

logo_time = 0.0


def enter():
    global image,  boy, grass, fallf, grade, font
    image = load_image('pause.png')
    boy = main_state.boy
    grass = main_state.grass
    fallf = main_state.fallf
    grade = main_state.grade
    font = main_state.font


def exit():
    global image, boy, grass, fallf, grade, font
    del (image)
    del (boy)
    del (grass)
    del (fallf)
    del (grade)
    del (font)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

def update(frame_time):
    global logo_time
    logo_time = (logo_time+1) % 2

def draw():
    clear_canvas()
    image.draw(400, 300)
    grass.draw()
    boy.draw()
    grade.draw()
    font.draw()

    # 떨어지는 장애물 떨어지는 코드
    for fallfs in fallf:
        fallfs.draw()
    update_canvas()


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


if __name__ == '__Pause__':
    main()


def pause():
    pass


def resume():
    pass
