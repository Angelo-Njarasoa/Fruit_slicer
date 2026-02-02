
import pygame
from pygame.locals import *
import time
import random

from src.coordinates import *
from src.game_over import *


# ================================================
# Constants
# ================================================
WINDOW_SIZE = (1000, 800)
CAPTION = "Gameplay"

RED   = (255, 0, 0)
GREEN = (150, 255, 150)

FRUIT_SIZE = (100, 100)

SCORE_FONT_SIZE = 40
BOMB_FONT_SIZE  = 80
BOMB_COLOR = (255, 220, 80)

ALL_STATES = ["pineapple", "watermelon", "ice", "bomb", "apple", "lemon"]


def gameplay_typing(screen=None):
    pygame.display.set_caption(CAPTION)
    police = pygame.font.SysFont("arial", SCORE_FONT_SIZE)

    # Load and scale images
    ball = pygame.image.load("Assets/images/pasteque-removebg-preview.png").convert_alpha()
    ball = pygame.transform.scale(ball, FRUIT_SIZE)

    pineaple = pygame.image.load("Assets/images/removepine.png").convert_alpha()
    pineaple = pygame.transform.scale(pineaple, FRUIT_SIZE)

    heart = pygame.image.load("Assets/images/heart-removebg-preview.png").convert_alpha()
    heart = pygame.transform.scale(heart, FRUIT_SIZE)

    ice = pygame.image.load("Assets/images/iceCut-removebg-preview.png").convert_alpha()
    ice = pygame.transform.scale(ice, FRUIT_SIZE)

    bomb = pygame.image.load("Assets/images/bomb-removebg-preview.png").convert_alpha()
    bomb = pygame.transform.scale(bomb, FRUIT_SIZE)

    apple = pygame.image.load("Assets/images/appaleCut-removebg-preview.png").convert_alpha()
    apple = pygame.transform.scale(apple, FRUIT_SIZE)

    lemon = pygame.image.load("Assets/images/lemon-removebg-preview.png").convert_alpha()
    lemon = pygame.transform.scale(lemon, FRUIT_SIZE)

    # Reusable rects
    bomb_rect = bomb.get_rect()
    ice_rect  = ice.get_rect()
    rect_heart = heart.get_rect()
    rect_pine  = pineaple.get_rect()
    rect       = ball.get_rect()
    apple_rect = apple.get_rect()
    lemon_rect = lemon.get_rect()

    # Backgrounds
    background = pygame.image.load("Assets/images/tropic_img.png").convert()
    background = pygame.transform.scale(background, WINDOW_SIZE)

    background2 = pygame.image.load("Assets/images/winter.png").convert()
    background2 = pygame.transform.scale(background2, WINDOW_SIZE)

    # Game variables
    clock = pygame.time.Clock()
    running = True

    v = 0
    strikes = 3
    ice_mode = False
    state = "watermelon"

    all_path = [
        weird_move,
        classic_move,
        coordinates2,
        cordinate3,
        cordinate_jump,
        trajectoire_325,
        trajectoire_465,
        trajectoire_600,
        trajectoire_670,
        trajectoire_735,
        trajectoire_900,
        coordinate_left,
        trajectoire_y320,
        trajectoire_y400,
        trajectoire_y750,
        cordinate_Right,
        trajectoire_nouvelle,
        trajectoire_y200,
    ]

    path   = random.choice(all_path)
    path3  = random.choice(all_path)
    path4  = random.choice(all_path)
    path5  = random.choice(all_path)
    path6  = random.choice(all_path)   # apple
    path7  = random.choice(all_path)   # lemon

    path_index  = 0
    path_index3 = 0
    path_index4 = 0
    path_index5 = 0
    path_index6 = 0
    path_index7 = 0

    # Music
    pygame.mixer.init()
    pygame.mixer.music.load("Assets/game_music.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    while running:
        clock.tick(110)

        for event in pygame.event.get():
            if event.type == QUIT:
                return v

            if event.type == KEYDOWN:
                if event.key == K_p:
                    v += 10
                    time.sleep(0.3)
                    path_index = 0
                    state = random.choice(ALL_STATES)

                elif event.key == K_a:
                    v += 10
                    time.sleep(0.3)
                    path_index3 = 0
                    state = random.choice(ALL_STATES)

                elif event.key == K_b:
                    path_index5 = 0
                    strikes -= 3
                    time.sleep(0.3)

                elif event.key == K_p:
                    v += 10
                    time.sleep(0.3)
                    path_index6 = 0
                    state = random.choice(ALL_STATES)

                elif event.key == K_c:          # Touche L pour citron
                    v += 10
                    time.sleep(0.3)
                    path_index7 = 0
                    state = random.choice(ALL_STATES)

                elif event.key == K_g:
                    ice_mode = True
                    path_index4 = 0
                    state = random.choice(ALL_STATES)
                    time.sleep(4)

        scoretxt = police.render("score:", True, RED)
        vstr = str(v)
        score_nb = police.render(vstr, True, (255, 0, 0))

        # Trajectory end checks
        if path_index >= len(path):
            strikes -= 1
            path = random.choice(all_path)
            state = random.choice(ALL_STATES)
            path_index = 0

        if path_index3 >= len(path3):
            strikes -= 1
            path3 = random.choice(all_path)
            state = random.choice(ALL_STATES)
            path_index3 = 0

        if path_index4 >= len(path4):
            path4 = random.choice(all_path)
            state = random.choice(ALL_STATES)
            path_index4 = 0

        if path_index5 >= len(path5):
            path5 = random.choice(all_path)
            state = random.choice(ALL_STATES)
            path_index5 = 0

        if path_index6 >= len(path6):
            strikes -= 1
            path6 = random.choice(all_path)
            state = random.choice(ALL_STATES)
            path_index6 = 0

        if path_index7 >= len(path7):
            strikes -= 1
            path7 = random.choice(all_path)
            state = random.choice(ALL_STATES)
            path_index7 = 0

        screen.fill(RED)

        if ice_mode:
            screen.blit(background2, (0, 0))
        else:
            screen.blit(background, (0, 0))

        ice_mode = False

        screen.blit(scoretxt, (400, 10))
        screen.blit(score_nb, (500, 10))

        if strikes == 3:
            screen.blit(heart, (325, 55))
        if strikes > 1:
            screen.blit(heart, (395, 55))
        if strikes > 0:
            screen.blit(heart, (475, 55))

        # Fruit display based on current state
        if state == "watermelon":
            if path_index < len(path):
                rect.center = path[path_index]
                path_index += 1
            else:
                strikes -= 1
                path = random.choice(all_path)
                path_index = 0
                rect.center = path[path_index]
            screen.blit(ball, rect)

        if state == "pineapple":
            if path_index3 < len(path3):
                rect_pine.center = path3[path_index3]
                path_index3 += 1
            else:
                path_index3 = 0
                strikes -= 1
                path3 = random.choice(all_path)
                rect_pine.center = path3[path_index3]
            screen.blit(pineaple, rect_pine)

        if state == "ice":
            if path_index4 < len(path4):
                ice_rect.center = path4[path_index4]
                path_index4 += 1
            else:
                path_index4 = 0
                path4 = random.choice(all_path)
                ice_rect.center = path4[path_index4]
            screen.blit(ice, ice_rect)

        if state == "bomb":
            if path_index5 < len(path5):
                bomb_rect.center = path5[path_index5]
                path_index5 += 1
            else:
                path_index5 = 0
                path5 = random.choice(all_path)
                bomb_rect.center = path5[path_index5]
                text_rect.center = path5[path_index5]
            screen.blit(bomb, bomb_rect)
         

        if state == "apple":
            if path_index6 < len(path6):
                apple_rect.center = path6[path_index6]
                path_index6 += 1
            else:
                path_index6 = 0
                path6 = random.choice(all_path)
                apple_rect.center = path6[path_index6]
            screen.blit(apple, apple_rect)

        if state == "lemon":
            if path_index7 < len(path7):
                lemon_rect.center = path7[path_index7]
                path_index7 += 1
            else:
                path_index7 = 0
                path7 = random.choice(all_path)
                lemon_rect.center = path7[path_index7]
            screen.blit(lemon, lemon_rect)

        # Game Over check
        if strikes <= 0:
            if strikes <= 0 and running:
               
                return v

        pygame.display.update()

    return v