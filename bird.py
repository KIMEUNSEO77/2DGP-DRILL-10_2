from pico2d import load_image, get_time

class Bird:
    def __init__(self, x=400, y=300):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1) % 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
    def handle_events(self):
        pass