import game_framework
import main_state
from pico2d import *
from DeadEffect import DeadEffection


name = "Paperf"
image = None
deadeffection = None
current_time = 0.0


def enter():
    global image, deadeffection
    deadeffection = DeadEffection()
    image = load_image('paper F.png')
    game_framework.reset_time()


def exit():
    global image,deadeffection
    del(image)
    del(deadeffection)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    deadeffection.draw()
    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass