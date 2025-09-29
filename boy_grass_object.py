from pico2d import *
import random

class Grass:
    #생성자함수, 초기화수행
    def __init__(self):  # 개체의 속성을 정의하고 초기값을 알려주는 기능
        # grass 객체의 속성을 정의하고 초기화
        self.image = load_image('grass.png')

    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():

    pass



reset_world()

while True:
    handle_events()
    update_world()
    render_world()
    delay(0.05)



close_canvas()
