import game_framework
from pico2d import *

import main_state


name = "PauseState"
image1 = None
boy = None
grass = None
fallf = None

logo_tim = 0.0


def enter():
    global image,  boy, grass, fallf
    image = load_image('pause.png')
    boy = main_state.boy
    grass = main_state.grass
    fallf = main_state.fallf


def exit():
    global image, boy, grass, fallf
    del (image)
    del (boy)
    del (grass)
    del (fallf)


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
    logo_time = (logo_tim+1)%2

def draw():
    global logo_tim
    clear_canvas()
    if ( (logo_tim+1)%2 == 0):
        image.draw(400,400)
    else:
        image.draw(10000,4000)
    grass.draw()
    main_state.boy.image.clip_draw(main_state.boy.frame * 100, 0, 100, 100, main_state.boy.x, main_state.boy.y)
    update_canvas()





def pause():
    pass


def resume():
    pass
