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

    def update(self):
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


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(0, 400)
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90)

    pass

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        pass


def reset_world():
    global running
    global grass
    global team
    running = True
    grass = Grass()

    team = [Boy() for _ in range(11)]
    
    pass

#게임 로직, 객체들의 상호작용을 시뮬레이션
def update_world():
    grass.update()
    for boy in team:
        boy.update() # 소년의 상호작용을 시뮬레이션 계산

    pass


def render_world():
    #월드의 객체들을 그린다
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    pass

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)



close_canvas()
