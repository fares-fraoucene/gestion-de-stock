import pygame
from button import Text


pygame.init()


WINDOWWIDTH = 800
WINDOWHEIGHT = 600
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Tableau De Bord')
text = Text()
bg = ("black")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 10 and pos[0] <= 205 and pos[1] >= 102 and pos[1] <= 120:
                pass
            if pos[0] >= 10 and pos[0] <= 215 and pos[1] >= 250 and pos[1] <= 270:
                pass
            if pos[0] >= 10 and pos[0] <= 240 and pos[1] >= 405 and pos[1] <= 420:
                pass

    screen.fill(bg)

    pygame.draw.rect(screen, (135, 206, 255), (0, 0, 270, 800))
    screen.blit(text.draw_text("Ajouter Produit"), (10, 100))
    # x = 10 y = 102 , x = 205 y =120 
    screen.blit(text.draw_text("Modifier Produit"), (10, 250))
    # x = 10  y =250  x = 215  y =270
    screen.blit(text.draw_text("Supprimer Produit"), (10, 400))
    # x=10 y = 405, x = 240 y = 420
    screen.blit(text.draw_text("Tableau de Bord"), (450, 50))

    pygame.display.flip()



