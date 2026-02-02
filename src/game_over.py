import pygame
from src.gameplay_typing import *


vie=0
def game_over(screen,score: int = 0):
    nb =str(score)
    screen = pygame.display.set_mode((1000, 800))
    image = pygame.image.load("Assets/images/gameover.png").convert_alpha()
    image = pygame.transform.scale(image,(1000,800))
    font = pygame.font.Font(None, 74)
    text_replay = font.render("Rejouer",True,"blue")
    replay_rect = pygame.Rect(420, 200, 200, 100)
    text_score = font.render(nb,True,"blue")
    score_rect = pygame.Rect(420, 350, 200, 100)
    play_text_rect = text_replay.get_rect(center=replay_rect.center)
    score_text_rect = text_score.get_rect(center=score_rect.center)

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit((image),(0,0))

        screen.blit(text_replay,play_text_rect)
        screen.blit(text_score,score_text_rect)
        pygame.draw.rect(screen,"blue",replay_rect, 5)
        pygame.draw.rect(screen,"blue",score_rect,5)

        pygame.display.flip()

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return False
             elif event.type == pygame.MOUSEBUTTONDOWN:
                 if replay_rect.collidepoint(event.pos):
                     #Call functions gameplay here
                    return True
    pygame.display.flip()
                   
                  
