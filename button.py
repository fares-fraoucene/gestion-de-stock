import pygame
pygame.init()

class Text:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 26)

    def draw_text(self,text):
        draw = self.font.render(text, True, (0, 0, 0))
        return draw


