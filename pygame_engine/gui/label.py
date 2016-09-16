""" Module docstring.

    Author: Ian Davis
"""
import logging
import pygame

from pygame_engine.data import color

from widget import PGEWidget


logger = logging.getLogger('root.gui')


class Label(PGEWidget):
    def __init__(self, name, text, size, parent, font_family=None, font_size=12, bold=False, italic=False, text_color=color.BLACK, surface=None):
        super(Label, self).__init__(name, size, parent, surface)
        self.text = text
        self.font = pygame.font.SysFont(font_family, font_size, bold, italic)
        self.color = text_color

    def paint(self):
        super(Label, self).paint()
        self.surface.blit(self.font.render(self.text, True, self.color), self.rect)
