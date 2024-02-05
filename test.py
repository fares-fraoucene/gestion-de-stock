import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text Area Example")

# Set up the text areas
text_area_rect1 = pygame.Rect(50, 50, 300, 200)
text_area_rect2 = pygame.Rect(450, 50, 300, 200)
text_area_color = pygame.Color('white')
text_area_text1 = ''
text_area_text2 = ''
font = pygame.font.Font(None, 32)
text_area_active1 = False
text_area_active2 = False

# Function to check if the mouse is inside a text area
def is_mouse_inside_text_area(rect):
    mouse_pos = pygame.mouse.get_pos()
    return rect.collidepoint(mouse_pos)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if text_area_active1:
                if event.key == K_RETURN:
                    print("Text Area 1:", text_area_text1)  # Do something with the entered text
                    text_area_text1 = ''
                elif event.key == K_BACKSPACE:
                    text_area_text1 = text_area_text1[:-1]
                else:
                    text_area_text1 += event.unicode
            elif text_area_active2:
                if event.key == K_RETURN:
                    print("Text Area 2:", text_area_text2)  # Do something with the entered text
                    text_area_text2 = ''
                elif event.key == K_BACKSPACE:
                    text_area_text2 = text_area_text2[:-1]
                else:
                    text_area_text2 += event.unicode
        elif event.type == MOUSEBUTTONDOWN:
            if is_mouse_inside_text_area(text_area_rect1):
                text_area_active1 = True
                text_area_active2 = False
            elif is_mouse_inside_text_area(text_area_rect2):
                text_area_active1 = False
                text_area_active2 = True
            else:
                text_area_active1 = False
                text_area_active2 = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the text areas
    if text_area_active1:
        pygame.draw.rect(screen, text_area_color, text_area_rect1)
    else:
        pygame.draw.rect(screen, (200, 200, 200), text_area_rect1)

    if text_area_active2:
        pygame.draw.rect(screen, text_area_color, text_area_rect2)
    else:
        pygame.draw.rect(screen, (200, 200, 200), text_area_rect2)

    text_surface1 = font.render(text_area_text1, True, (0, 0, 0))
    text_surface2 = font.render(text_area_text2, True, (0, 0, 0))

    screen.blit(text_surface1, (text_area_rect1.x + 10, text_area_rect1.y + 10))
    screen.blit(text_surface2, (text_area_rect2.x + 10, text_area_rect2.y + 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()