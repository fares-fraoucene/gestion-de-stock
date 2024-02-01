import pygame


pygame.init()


WINDOWWIDTH = 800
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Tableau De Bord')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    windowSurface.fill((255, 255, 255))

    pygame.display.flip()


