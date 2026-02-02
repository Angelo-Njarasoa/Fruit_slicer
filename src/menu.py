import pygame
import sys

def menu(screen):

    

    # screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Fruit Slicer !")
    image = pygame.image.load("Assets/images/bkrgd_fruit_men.png").convert()
    image = pygame.transform.scale(image,(1000,800))
    font = pygame.font.Font(None, 74)

    #Initialized  text from the menu.
    text_play = font.render("Jouer", True, "blue")
    text_quit = font.render("Quitter", True, "blue")

   # text_options = font.render("ajout mot", True, (248, 37, 217))
    #Initialized buttons from menu
    play_rect = pygame.Rect(400, 220, 200, 100)
    quit_rect = pygame.Rect(400, 370, 200, 100)
    play_text_rect = text_play.get_rect(center=play_rect.center)
    quit_text_rect = text_quit.get_rect(center=quit_rect.center)
    #options_rect = pygame.Rect(550, 350, 250, 100)



    pygame.mixer.music.load("Assets/Crash_Bandicoot.mp3")
    pygame.mixer.music.play(-1)
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit((image),(0,0))

        screen.blit(text_play,play_text_rect)
        screen.blit(text_quit,quit_text_rect )
        
        #screen.blit(text_options, (options_rect.x, options_rect.y))
        
        pygame.draw.rect(screen,"blue",play_text_rect, 5)
        pygame.draw.rect(screen, "blue", quit_text_rect, 5)
        #pygame.draw.rect(screen, (0, 0, 0), options_rect, 1)
        pygame.mixer.init(frequency=16000)
       
        

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    #Call functions gameplay here
                    return "play"
                elif quit_rect.collidepoint(event.pos):
                    #Call functions word here
                    print("Au revoir !")
                    return"quit"
                

