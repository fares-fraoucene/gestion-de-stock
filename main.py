import pygame
from button import Button


pygame.init()


WINDOWWIDTH = 800
WINDOWHEIGHT = 600
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Tableau De Bord')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (135, 206, 255), (0, 0, 270, 800))
    screen.blit(Button.draw_text("Salut"), (0, 0))
    pygame.display.flip()



