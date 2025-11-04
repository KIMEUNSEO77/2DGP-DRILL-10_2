from pico2d import *
import game_world
import game_framework
#from boy import PIXEL_PER_METER

PIXEL_PER_METER = 1.0 / 0.03   # 1cm = 3 pixel
GRAVITY = 9.8   # 중력 가속도


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, throwin_speed = 15, throwin_angle = 45):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.xv = throwin_speed * math.cos(math.radians(throwin_angle))
        self.vy = abs(throwin_speed * math.sin(math.radians(throwin_angle)))  # 항상 양수로 시작

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        '''
        self.x += self.velocity * game_framework.frame_time * PIXEL_PER_METER

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
            '''

        self.vy -= GRAVITY * game_framework.frame_time   # v = at

        self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER
        self.y += self.vy * game_framework.frame_time * PIXEL_PER_METER

        if self.y < 60:
            game_world.remove_object(self)

