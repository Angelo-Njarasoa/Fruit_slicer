from src.menu import *
from src.gameplay_typing import gameplay_typing
from src.game_over import game_over

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Fruit Slicer !")
clock = pygame.time.Clock()

while True:
    action=menu(screen)
    if action== "quit" or action == None:
        break
    while True:
        score = gameplay_typing(screen)
        replay = game_over(screen, score)

    
        if not replay:
            break
pygame.quit 