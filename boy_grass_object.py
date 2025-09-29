from pico2d import *
import random

class Grass:
    #생성자함수, 초기화수행
    def __init__(self):  # 개체의 속성을 정의하고 초기값을 알려주는 기능
        # grass 객체의 속성을 정의하고 초기화
        self.image = load_image('grass.png')

    pass

    def draw(self):
        self.image.draw(400, 30)
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
    global running
    global grass
    
    running = True
    grass = Grass()
    pass

def update_world():
    pass


def render_world():
    #월드의 객체들을 그린다
    clear_canvas()
    grass.draw()
    update_canvas()
    pass

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)



close_canvas()
