import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ma fenêtre Pygame")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up font
font = pygame.font.Font(None, 36)

class Text:
    def __init__(self, text, color, font, position) -> None:
        self.text = text
        self.color = color
        self.font = font
        self.position = position

    def draw_text(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=self.position)
        return text_surface, text_rect

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Example of using the Text class
    text_obj = Text("Salut", white, font, (100, 100))
    text_surface, text_rect = text_obj.draw_text()
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()
