from pico2d import load_image, get_time

import game_framework

PIXEL_PER_METER = (10.0 / 0.25)   # 10 pixel 25 cm
RUN_SPEED_KMPH = 10.0              # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)    # meter / minute
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)    # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)   # pixel / second

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    def __init__(self, x=400, y=300):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1   # 1: right, -1: left

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw((int)(self.frame) * 100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_composite_draw((int)(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, 100, 100)

    def handle_events(self):
        pass