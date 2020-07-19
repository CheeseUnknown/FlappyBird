import pygame, random
from pygame.locals import *

FPS = 120
transparent = 0, 0, 0, 0

screen_width = 288
screen_height = 512
main_screen_background_day = pygame.image.load("image/bg_day.png")
main_screen_background_night = pygame.image.load("image/bg_night.png")
main_screen_land = pygame.image.load("image/land.png")

ready_screen_play_button = pygame.image.load("image/button_play.png")
ready_screen_title = pygame.image.load("image/title.png")

bird_style = random.randint(0, 2)
bird00 = pygame.image.load("image/bird0_0.png")
bird01 = pygame.image.load("image/bird0_1.png")
bird02 = pygame.image.load("image/bird0_2.png")
bird10 = pygame.image.load("image/bird1_0.png")
bird11 = pygame.image.load("image/bird1_1.png")
bird12 = pygame.image.load("image/bird1_2.png")
bird20 = pygame.image.load("image/bird2_0.png")
bird21 = pygame.image.load("image/bird2_1.png")
bird22 = pygame.image.load("image/bird2_2.png")

pipe_up = pygame.image.load("image/pipe_up.png")
pipe_down = pygame.image.load("image/pipe_down.png")

beginning_screen_tutorial = pygame.image.load("image/tutorial.png")
beginning_screen_ready = pygame.image.load("image/text_ready.png")

gaming_screen_letter = [pygame.image.load("image/font_048.png"),
    pygame.image.load("image/font_049.png"),
    pygame.image.load("image/font_050.png"),
    pygame.image.load("image/font_051.png"),
    pygame.image.load("image/font_052.png"),
    pygame.image.load("image/font_053.png"),
    pygame.image.load("image/font_054.png"),
    pygame.image.load("image/font_055.png"),
    pygame.image.load("image/font_056.png"),
    pygame.image.load("image/font_057.png"),
]

dead_screen_game_over = pygame.image.load("image/text_game_over.png")
dead_screen_score_board = pygame.image.load("image/score_panel.png")
dead_screen_bronze_medal = pygame.image.load("image/medals_3.png")
dead_screen_silver_medal = pygame.image.load("image/medals_2.png")
dead_screen_gold_medal = pygame.image.load("image/medals_1.png")
dead_screen_restart_button = pygame.image.load("image/button_play.png")

dead_screen_score_board_letter = [
    pygame.image.load("image/number_score_00.png"),
    pygame.image.load("image/number_score_01.png"),
    pygame.image.load("image/number_score_02.png"),
    pygame.image.load("image/number_score_03.png"),
    pygame.image.load("image/number_score_04.png"),
    pygame.image.load("image/number_score_05.png"),
    pygame.image.load("image/number_score_06.png"),
    pygame.image.load("image/number_score_07.png"),
    pygame.image.load("image/number_score_08.png"),
    pygame.image.load("image/number_score_09.png"),
]

class Setting(object):
    def __init__(self):
        self.best_score = 0
        with open("setting/setting.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')
                if line.startswith('bestscore:'):
                    self.best_score = int(line.split(":", 1)[1])
        # 0:ready 1:begining 2:playing 3:dead
        self.phase = 0
        self.score = 0