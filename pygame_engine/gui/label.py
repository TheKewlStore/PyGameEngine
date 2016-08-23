""" Module docstring.

    Author: Ian Davis
"""
import pygame

from widget import PGEWidget


class Label(PGEWidget):
    def __init__(self, text, size, font_family=None, font_size=12, bold=False, italic=False, surface=None, layout=None):
        super(Label, self).__init__(size, surface, layout)
        self.text = text
        self.font = pygame.font.SysFont(font_family, font_size, bold, italic)

    def paint(self):
        self.surface.blit(self.font.render(self.text))
