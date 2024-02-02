import pygame
from button import *
from product import Product

pygame.init()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Tableau De Bord')
text = Text()
product = Product()
screen_state = "ecran_principal"

def afficher_donnees(donnees):
    taille_case_x = 110
    taille_case_y = 50
    decalage_x, decalage_y = 200, 130

    for i, ligne in enumerate(donnees):
        for j, valeur in enumerate(ligne):
            x = j * taille_case_x + decalage_x
            y = i * taille_case_y + decalage_y
            pygame.draw.rect(screen, "white", (x, y, taille_case_x, taille_case_y))
            font = pygame.font.Font(None, 20)
            texte = font.render(str(valeur), True, "black")
            screen.blit(texte, (x + 20, y + 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 10 <= pos[0] <= 205 and 102 <= pos[1] <= 120:
                screen_state = "ajouter_produit"
            if 10 <= pos[0] <= 215 and 250 <= pos[1] <= 270:
                screen_state = "modifier_produit"
            if 10 <= pos[0] <= 240 and 405 <= pos[1] <= 420:
                screen_state = "supprimer_produit"

    screen.fill("white")

    if screen_state == "ecran_principal":
        donnees = product.get_all_products()
        afficher_donnees(donnees)
        screen.blit(text.draw_text("Tableau de Bord"), (450, 50))
        screen.blit(text.draw_text("Id"), (220, 100))
        screen.blit(text.draw_text("Nom"), (330, 100))
        screen.blit(text.draw_text("Description"), (420, 100))
        screen.blit(text.draw_text("Prix"), (540, 100))
        screen.blit(text.draw_text("Quantité"), (620, 100))
        screen.blit(text.draw_text("Id Catégorie"), (700, 100))
        pygame.display.flip()

    elif screen_state == "ajouter_produit":
        screen.blit(text.draw_text("Ajouter Produit"), (390, 100))
        pygame.display.flip()

    pygame.draw.rect(screen, (135, 206, 255), (0, 0, 200, 800))
    screen.blit(text.draw_text("Ajouter Produit"), (10, 100))
    screen.blit(text.draw_text("Modifier Produit"), (10, 250))
    screen.blit(text.draw_text("Supprimer Produit"), (10, 400))
    pygame.display.flip()
