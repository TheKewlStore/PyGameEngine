""" Module docstring.

    Author: Ian Davis
"""
import pygame

from pygame_engine.data import color

from widget import PGEWidget


class Label(PGEWidget):
    def __init__(self, text, size, font_family=None, font_size=12, bold=False, italic=False, text_color=color.BLACK, surface=None, layout=None):
        super(Label, self).__init__(size, surface, layout)
        self.text = text
        self.font = pygame.font.SysFont(font_family, font_size, bold, italic)
        self.color = text_color

    def paint(self):
        self.surface.blit(self.font.render(self.text, True, self.color), self.rect)
