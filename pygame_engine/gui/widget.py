""" Define the base widget to be used by layouts and displays.

    Author: Ian Davis
"""
# TODO: Setup basic widgets such as buttons and labels.
import pygame

from pygame_engine.data import Point
from pygame_engine.gui.layout import VerticalLayout


class PGEWidget(object):
    def __init__(self, size, surface=None, layout=None):
        self.size = size
        self.surface = surface
        self.layout = layout

    @property
    def rect(self):
        if self.layout:
            origin = self.layout.get_origin(self)
        else:
            origin = Point(0, 0)

        return pygame.Rect(origin.x, origin.y, self.size.width, self.size.height)

    def paint(self):
        if self.layout:
            self.layout.paint_widgets()


class PGERootWidget(PGEWidget):
    def __init__(self, size, surface=None):
        super(PGERootWidget, self).__init__(size, surface)

        self.layout = VerticalLayout('root', self.size.width, self.size.height, self)

    @property
    def rect(self):
        return pygame.Rect(0, 0, self.size.width, self.size.height)
