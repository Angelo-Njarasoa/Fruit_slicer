import pygame
from pygame.locals import *

size = 1200, 980
width, height = size
GREEN = (150, 255, 150)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

ball = pygame.image.load("pasteque.jpg").convert()
ball=pygame.transform.scale(ball,(70,70))
rect = ball.get_rect()
speed = [1, 1]

while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and rect.collidepoint(event.pos):
                     
                    
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()

pygame.quit()