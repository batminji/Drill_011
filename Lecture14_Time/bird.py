# 이것은 각 상태들을 객체로 구현한 것임.
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 50.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14
FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ACTION

from pico2d import*
import game_world
import game_framework

class Bird:
    def __init__(self):
        self.x, self.y = 400, 300
        self.frame = 0
        self.action = 2
        self.dir = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        temp_frame = 0.0
        temp_frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.frame = temp_frame % 5
        self.action = temp_frame / 5
        if int(self.action) == 0 and int(self.frame) == 4:
            self.action, self.frame = 2, 0

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x >= 1550:
            self.dir = -1
        elif self.x <= 50:
            self.dir = 1

    def handle_event(self, event):
        pass

    def draw(self):
        if self.dir == 1 : # 오른쪽으로이동
            self.image.clip_composite_draw(int(self.frame) * 183, int(self.action) * 168, 183, 168, 0, '', self.x, self.y, 100, 100)

        else :
            self.image.clip_composite_draw(int(self.frame) * 183, int(self.action) * 168, 183, 168, 0, 'h', self.x, self.y, 100, 100)
