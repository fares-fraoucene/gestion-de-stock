import pygame
import sqlite3
import sys

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Affichage d'une base de données SQLite avec Pygame")

# Définir les couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Fonction pour récupérer les données de la base de données
def recuperer_donnees():
    connexion = sqlite3.connect("ma_base_de_donnees.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM ma_table")
    donnees = curseur.fetchall()
    connexion.close()
    return donnees

# Fonction pour afficher les données dans la fenêtre
def afficher_donnees(donnees):
    taille_case = 50
    for i, ligne in enumerate(donnees):
        for j, valeur in enumerate(ligne):
            pygame.draw.rect(fenetre, blanc, (j * taille_case, i * taille_case, taille_case, taille_case))
            font = pygame.font.Font(None, 36)
            texte = font.render(str(valeur), True, noir)
            fenetre.blit(texte, (j * taille_case + 20, i * taille_case + 20))

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    fenetre.fill(noir)

    # Récupérer les données de la base de données
    donnees = recuperer_donnees()

    # Afficher les données
    afficher_donnees(donnees)

    # Mettre à jour l'écran
    pygame.display.flip()
