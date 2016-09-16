""" Define the base widget to be used by layouts and displays.

    Author: Ian Davis
"""
# TODO: Setup basic widgets such as buttons and labels.
import logging
import pygame

from pygame_engine.data import Point
from pygame_engine.gui.layout import VerticalLayout


logger = logging.getLogger('root.gui')


class PGEWidget(object):
    def __init__(self, name, size, parent=None, surface=None):
        self.name = name
        self.size = size
        self.surface = surface
        self.layout = VerticalLayout('{0}_layout'.format(self.name), self.size.width, self.size.height, self)
        self.parent = parent
        self.origin = Point(0, 0)
        self.needs_repaint = True

    @property
    def rect(self):
        return pygame.Rect(self.origin.x, self.origin.y, self.size.width, self.size.height)

    def get_origin(self, widget):
        return self.layout.get_origin(widget)

    def paint(self):
        if not self.needs_repaint:
            return

        logger.debug('Painting widget {0}'.format(self))

        if self.layout:
            self.layout.paint_widgets()

        self.needs_repaint = False

    def __str__(self):
        return '{0}{1}'.format(self.name, self.rect)

    def __repr__(self):
        return '{0}(name={1}, rect={2})'.format(self.__class__.__name__, self.name, self.rect)
