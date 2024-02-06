import pygame
from button import *
from product import *

pygame.init()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Tableau De Bord')
text = Text()
product = Product()
screen_state = "ecran_principal"
text_area_text1 = ''
text_area_text2 = ''
text_area_text3 = ''
text_area_text4 = ''
text_area_text5 = ''
text_area_text6 = ''
text_area_text7 = ''
text_area_text8 = ''
text_area_text8 = ''
text_area_text9 = ''
text_area_rect1 = pygame.Rect(260, 200, 500, 30)
text_area_rect2 = pygame.Rect(260, 260, 500, 30)
text_area_rect3 = pygame.Rect(260, 320, 500, 30)
text_area_rect4 = pygame.Rect(260, 380, 500, 30)
text_area_rect5 = pygame.Rect(260, 440, 500, 30)
text_area_rect6 = pygame.Rect(260, 200, 500, 30)
text_area_rect7 = pygame.Rect(260, 200, 500, 30)
text_area_rect8 = pygame.Rect(260, 260, 500, 30)
text_area_rect9 = pygame.Rect(260, 320, 500, 30)

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

def is_mouse_inside_text_area(rect):
    mouse_pos = pygame.mouse.get_pos()
    return rect.collidepoint(mouse_pos)

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
            if 10 <= pos[0] <= 100 and 550 <= pos[1] <= 570:
                screen_state = "ecran_principal"
            if screen_state == "ajouter_produit" and 260 <= pos[0] <= 340 and 500 <= pos[1] <= 520:
                product.add_product(text_area_text1, text_area_text2, text_area_text3, text_area_text4, text_area_text5)
                screen_state = "ecran_principal"
                text_area_text1 = ''
                text_area_text2 = ''
                text_area_text3 = ''
                text_area_text4 = ''
                text_area_text5 = ''
            if screen_state == "supprimer_produit" and 260 <= pos[0] <= 340 and 250 <= pos[1] <= 270:
                product.delete_product(text_area_text6)
                screen_state = "ecran_principal"
                text_area_text6 = ''
            if screen_state == "modifier_produit" and 260 <= pos[0] <= 340 and 370 <= pos[1] <= 390:
                product.update_product(text_area_text7, text_area_text8, text_area_text9)
                screen_state = "ecran_principal"
                text_area_text7 = ''
                text_area_text8 = ''
                text_area_text9 = ''
            
        if event.type == pygame.KEYDOWN:
            if text_area_active1 and screen_state == "ajouter_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 1:", text_area_text1)  
                    text_area_text1 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text1 = text_area_text1[:-1]
                else:
                    text_area_text1 += event.unicode
            elif text_area_active2 and screen_state == "ajouter_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 2:", text_area_text2)
                    text_area_text2 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text2 = text_area_text2[:-1]
                else:
                    text_area_text2 += event.unicode
            elif text_area_active3 and screen_state == "ajouter_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 3:", text_area_text3)
                    text_area_text3 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text3 = text_area_text3[:-1]
                else:
                    text_area_text3 += event.unicode
            elif text_area_active4 and screen_state == "ajouter_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 4:", text_area_text4)
                    text_area_text4 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text4 = text_area_text4[:-1]
                else:
                    text_area_text4 += event.unicode
            elif text_area_active5 and screen_state == "ajouter_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 5:", text_area_text5)
                    text_area_text5 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text5 = text_area_text5[:-1]
                else:
                    text_area_text5 += event.unicode
            elif text_area_active6 and screen_state == "supprimer_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 6:", text_area_text6)
                    text_area_text6 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text6 = text_area_text6[:-1]
                else:
                    text_area_text6 += event.unicode
            elif text_area_active7 and screen_state == "modifier_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 7:", text_area_text7)
                    text_area_text7 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text7 = text_area_text7[:-1]
                else:
                    text_area_text7 += event.unicode
            elif text_area_active8 and screen_state == "modifier_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 8:", text_area_text8)
                    text_area_text8 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text8 = text_area_text8[:-1]
                else:
                    text_area_text8 += event.unicode
            elif text_area_active9 and screen_state == "modifier_produit":
                if event.key == pygame.K_RETURN:
                    print("Text Area 9:", text_area_text9)
                    text_area_text9 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text_area_text9 = text_area_text9[:-1]
                else:
                    text_area_text9 += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_mouse_inside_text_area(text_area_rect1) and screen_state == "ajouter_produit":
                text_area_active1 = True
                text_area_active2 = False
                text_area_active3 = False
                text_area_active4 = False
                text_area_active5 = False
                text_area_active6 = False
                text_area_active7 = False
                text_area_active8 = False
                text_area_active9 = False
            elif is_mouse_inside_text_area(text_area_rect2) and screen_state == "ajouter_produit":
                text_area_active1 = False
                text_area_active2 = True
                text_area_active3 = False
                text_area_active4 = False
                text_area_active5 = False
                text_area_active6 = False
                text_area_active7 = False
                text_area_active8 = False
                text_area_active9 = False
            elif is_mouse_inside_text_area(text_area_rect3) and screen_state == "ajouter_produit":
                text_area_active1 = False
                text_area_active2 = False
                text_area_active3 = True
                text_area_active4 = False
                text_area_active5 = False
                text_area_active6 = False
                text_area_active7 = False
                text_area_active8 = False
                text_area_active9 = False
            elif is_mouse_inside_text_area(text_area_rect4) and screen_state == "ajouter_produit":
                text_area_active1 = False
                text_area_active2 = False
                text_area_active3 = False
                text_area_active4 = True
                text_area_active5 = False
                text_area_active6 = False
                text_area_active7 = False
                text_area_active8 = False
                text_area_active9 = False
            elif is_mouse_inside_text_area(text_area_rect5) and screen_state == "ajouter_produit":
                text_area_active1 = False
                text_area_active2 = False
                text_area_active3 = False
                text_area_active4 = False
                text_area_active5 = True
                text_area_active6 = False
                text_area_active7 = False
                text_area_active8 = False
                text_area_active9 = False
            elif is_mouse_inside_text_area(text_area_rect6) and screen_state == "supprimer_produit":
                text_area_active1 = False
                text_area_active2 = False
                text_area_active3 = False
                text_area_active4 = False
                text_area_active5 = False
                text_area_active6 = True
                text_area_active7 = False
                text_area_active8 = False
                text_area_active9 = False
            elif is_mouse_inside_text_area(text_area_rect7) and screen_state == "modifier_produit":
                text_area_active1 = False
                text_area_active2 = False
                text_area_active3 = False
                text_area_active4 = False
                text_area_active5 = False
                text_area_active6 = False
                text_area_active7 = True
                text_area_active8 = False
                text_area_active9 = False
            elif is_mouse_inside_text_area(text_area_rect8) and screen_state == "modifier_produit":
                text_area_active1 = False
                text_area_active2 = False
                text_area_active3 = False
                text_area_active4 = False
                text_area_active5 = False
                text_area_active6 = False
                text_area_active7 = False
                text_area_active8 = True
                text_area_active9 = False
            elif is_mouse_inside_text_area(text_area_rect9) and screen_state == "modifier_produit":
                text_area_active1 = False
                text_area_active2 = False
                text_area_active3 = False
                text_area_active4 = False
                text_area_active5 = False
                text_area_active6 = False
                text_area_active7 = False
                text_area_active8 = False
                text_area_active9 = True
            else:
                text_area_active1 = False
                text_area_active2 = False
                text_area_active3 = False
                text_area_active4 = False
                text_area_active5 = False
                text_area_active6 = False
                text_area_active7 = False
                text_area_active8 = False
                text_area_active9 = False
    screen.fill("white")
    if screen_state == "ecran_principal":
        pygame.draw.rect(screen, ("blue"), (0, 0, 200, 800))
        screen.blit(text.draw_text("Ajouter Produit"), (10, 100))
        screen.blit(text.draw_text("Modifier Produit"), (10, 250))
        screen.blit(text.draw_text("Supprimer Produit"), (10, 400))
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
        pygame.draw.rect(screen, ("blue"), (0, 0, 200, 800))
        screen.blit(text.draw_text("Ajouter Produit"), (10, 100))   
        screen.blit(text.draw_text("Modifier Produit"), (10, 250))
        screen.blit(text.draw_text("Supprimer Produit"), (10, 400))
        screen.blit(text.draw_text("Ajouter Produit"), (390, 100))
        screen.blit(text.draw_text("Nom :"), (260, 180))
        screen.blit(text.draw_text("Description :"), (260, 240))
        screen.blit(text.draw_text("Prix :"), (260, 300))
        screen.blit(text.draw_text("Quantité :"), (260, 360))
        screen.blit(text.draw_text("Id Catégorie :"), (260, 420))
        screen.blit(text.draw_text("Retour"), (10, 550))
        screen.blit(text.draw_text('Envoyer'), (260, 500))
        pygame.draw.rect(screen, "gray", text_area_rect1)
        pygame.draw.rect(screen, "gray", text_area_rect2)
        pygame.draw.rect(screen, "gray", text_area_rect3)
        pygame.draw.rect(screen, "gray", text_area_rect4)
        pygame.draw.rect(screen, "gray", text_area_rect5)
        screen.blit(text.draw_text(text_area_text1), (260,205))
        screen.blit(text.draw_text(text_area_text2), (260,265))
        screen.blit(text.draw_text(text_area_text3), (260,325))
        screen.blit(text.draw_text(text_area_text4), (260,385))
        screen.blit(text.draw_text(text_area_text5), (260,445))
        pygame.display.flip()
    elif screen_state == "modifier_produit":
        pygame.draw.rect(screen, ("blue"), (0, 0, 200, 800))
        screen.blit(text.draw_text("Ajouter Produit"), (10, 100))
        screen.blit(text.draw_text("Modifier Produit"), (10, 250))
        screen.blit(text.draw_text("Supprimer Produit"), (10, 400))
        screen.blit(text.draw_text("Modifier Produit"), (390, 100))
        screen.blit(text.draw_text("Modifier produit"), (260, 200))
        screen.blit(text.draw_text("Retour"), (10, 550))
        screen.blit(text.draw_text('Envoyer'), (260, 370))
        pygame.draw.rect(screen, "gray", text_area_rect7)
        pygame.draw.rect(screen, "gray", text_area_rect8)
        pygame.draw.rect(screen, "gray", text_area_rect9)
        screen.blit(text.draw_text("Nom Colonne: (eng)"), (260, 180))
        screen.blit(text.draw_text("Nouvelle Valeur:"), (260, 240))
        screen.blit(text.draw_text("Id Produit:"), (260, 300))
        screen.blit(text.draw_text(text_area_text7),(260, 200))
        screen.blit(text.draw_text(text_area_text8),(260, 260))
        screen.blit(text.draw_text(text_area_text9),(260, 320))
        pygame.display.flip()
    elif screen_state == "supprimer_produit":
        pygame.draw.rect(screen, ("blue"), (0, 0, 200, 800))
        screen.blit(text.draw_text("Ajouter Produit"), (10, 100))
        screen.blit(text.draw_text("Modifier Produit"), (10, 250))
        screen.blit(text.draw_text("Supprimer Produit"), (10, 400))
        screen.blit(text.draw_text("Supprimer Produit"), (390, 100))
        screen.blit(text.draw_text("Nom :"), (260, 200))
        pygame.draw.rect(screen, "gray", text_area_rect6)
        screen.blit(text.draw_text(text_area_text6), (260, 205))
        screen.blit(text.draw_text("Nom produit:"), (260, 180))
        screen.blit(text.draw_text("valider"), (260, 250))
        screen.blit(text.draw_text("Retour"), (10, 550))
        pygame.display.flip()
    pygame.display.flip()
