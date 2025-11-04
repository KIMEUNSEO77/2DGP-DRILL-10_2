import random

from pico2d import *

from boy import Boy
from grass import Grass
import game_world
from bird import Bird

import game_framework


boy = None
bird = []

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global running
    global bird

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    x, y = 100, 400
    for i in range(10):
        bird = Bird(x + i * 150, y)
        game_world.add_object(bird, 1)





def update():
    game_world.update()
    delay(0.1)  # 딜레이

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

