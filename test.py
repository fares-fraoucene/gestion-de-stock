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
screen_state = "tableau_de_bord"

# Ajout de cases pour écrire
input_rect1 = pygame.Rect(250, 150, 140, 32)
input_rect2 = pygame.Rect(250, 200, 140, 32)
input_rect3 = pygame.Rect(250, 250, 140, 32)
input_rect4 = pygame.Rect(250, 300, 140, 32)

font = pygame.font.Font(None, 32)
input_text1 = ""
input_text2 = ""
input_text3 = ""
input_text4 = ""

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

    if screen_state == "ecran_principal":
        screen.fill("white")
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
        screen.fill("black")
        
        pygame.draw.rect(screen, (135, 206, 255), input_rect1)
        pygame.draw.rect(screen, (135, 206, 255), input_rect2)
        pygame.draw.rect(screen, (135, 206, 255), input_rect3)
        pygame.draw.rect(screen, (135, 206, 255), input_rect4)
        
        font = pygame.font.Font(None, 32)
        
        pygame.draw.rect(screen, (255, 255, 255), input_rect1, 2)
        pygame.draw.rect(screen, (255, 255, 255), input_rect2, 2)
        pygame.draw.rect(screen, (255, 255, 255), input_rect3, 2)
        pygame.draw.rect(screen, (255, 255, 255), input_rect4, 2)

        text_surface1 = font.render(input_text1, True, (255, 255, 255))
        text_surface2 = font.render(input_text2, True, (255, 255, 255))
        text_surface3 = font.render(input_text3, True, (255, 255, 255))
        text_surface4 = font.render(input_text4, True, (255, 255, 255))

        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        screen.blit(text_surface3, (input_rect3.x + 5, input_rect3.y + 5))
        screen.blit(text_surface4, (input_rect4.x + 5, input_rect4.y + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Produit ajouté avec succès!")
                    # Ajoutez ici votre logique pour ajouter le produit avec les données des cases de texte
                elif event.key == pygame.K_BACKSPACE:
                    if input_rect1.collidepoint(event.pos):
                        input_text1 = input_text1[:-1]
                    if input_rect2.collidepoint(event.pos):
                        input_text2 = input_text2[:-1]
                    if input_rect3.collidepoint(event.pos):
                        input_text3 = input_text3[:-1]
                    if input_rect4.collidepoint(event.pos):
                        input_text4 = input_text4[:-1]
                else:
                    if input_rect1.collidepoint(event.pos):
                        input_text1 += event.unicode
                    if input_rect2.collidepoint(event.pos):
                        input_text2 += event.unicode
                    if input_rect3.collidepoint(event.pos):
                        input_text3 += event.unicode
                    if input_rect4.collidepoint(event.pos):
                        input_text4 += event.unicode

    pygame.draw.rect(screen, (135, 206, 255), (0, 0, 200, 800))
    screen.blit(text.draw_text("Ajouter Produit"), (10, 100))
    screen.blit(text.draw_text("Modifier Produit"), (10, 250))
    screen.blit(text.draw_text("Supprimer Produit"), (10, 400))
    pygame.display.flip()
