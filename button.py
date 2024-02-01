import pygame
pygame.init()

class Button:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        
    def draw_text(self,text):
        text = self.font.render(text, True, (0, 0, 0))
        return text


