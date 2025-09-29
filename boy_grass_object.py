from pico2d import *
import random

class Grass:
    #생성자함수, 초기화수행
    def __init__(self):  # 개체의 속성을 정의하고 초기값을 알려주는 기능
        # grass 객체의 속성을 정의하고 초기화
        self.image = load_image('grass.png')

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
        self.frame = random.randint(0, 7)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        pass

class Zombie:

    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
        self.x, self.y, frame_width // 2, frame_height // 2)


class Ball_1:

    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(100, 700)
        self.y = 599
        self.speed = random.randint(2, 5)
    def draw(self):
        self.image.draw (self.x, self.y)
    def update(self):
        self.y -= self.speed
        if self.y < 60:
            self.y = 60

class Ball_2:

    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(100, 700)
        self.y = 599
        self.speed = random.randint(2, 5)

    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.y -= self.speed
        if self.y < 70:
            self.y = 70

def reset_world():
    global running

    global world # world list = 모든 객체들을 갖고있는 리스트

    world = [] # 하나도 객체가 없는 월드
    running = True

    #땅을 만들고 월드에 추가
    grass = Grass()
    world.append(grass)

    #소년 11명을 만들고 월드에 추가
    team = [Boy() for _ in range(11)]
    world += team

    zombie = Zombie()
    world.append(zombie)

    balls_1 = [Ball_1() for _ in range(10)]
    world += balls_1

    balls_2 = [Ball_2() for _ in range(10)]
    world += balls_2
    
    pass


#게임 로직, 객체들의 상호작용을 시뮬레이션
def update_world():
    for game_object in world:
        game_object.update()

    pass


def render_world():
    #월드의 객체들을 그린다
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()
    pass

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
