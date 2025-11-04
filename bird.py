from pico2d import load_image, get_time

import game_framework

PIXEL_PER_METER = (10.0 / 0.25)   # 10 pixel 25 cm
RUN_SPEED_KMPH = 10.0              # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)    # meter / minute
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)    # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)   # pixel / second

class Bird:
    def __init__(self, x=400, y=300):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1   # 1: right, -1: left

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def handle_events(self):
        pass