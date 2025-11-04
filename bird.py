from pico2d import load_image, get_time

import game_framework

PIXEL_PER_METER = (10.0 / 0.3)   # 10 pixel 20 cm
RUN_SPEED_KMPH = 10.0              # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)    # meter / minute
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)    # meter / second
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)   # pixel / second

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    def __init__(self, x=400, y=300, frame_idx=0):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        # self.frame = 0
        self.dir = 1   # 1: right, -1: left
        self.frame_x = [35, 215, 385, 580, 35, 215, 385, 580, 760, 35, 215, 385, 580, 760]
        self.frame_y = [0, 0, 0, 0, 170, 170, 170, 170, 170, 350, 350, 350, 350, 350]
        self.frame_idx = frame_idx
        self.frame = (int) (frame_idx)

    def update(self):
        # self.frame_idx = (self.frame_idx + 1) % 14
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.x > 1600:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1

    def draw(self):
        self.frame_idx = (int)(self.frame)
        if self.dir == 1:
            self.image.clip_composite_draw(self.frame_x[self.frame_idx], self.frame_y[self.frame_idx], 140, 160, 0, '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame_x[self.frame_idx], self.frame_y[self.frame_idx], 140, 160, 0, 'h', self.x, self.y, 100, 100)

    def handle_events(self):
        pass