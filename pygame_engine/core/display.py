""" Define the Display class, which manages the main window of the engine.

    Author: Ian Davis
"""
import pygame

from pygame_engine.core.engine import Engine
from pygame_engine.lib.gui.widget import PGERootWidget


class Display(object):
    """ Represent a main display window for the PyGameEngine.
    """
    def __init__(self, size, main_widget=None):
        self._main_widget = main_widget
        self.surface = pygame.display.set_mode(size)
        self.size = size
        self._register_default_callbacks()

        if self._main_widget:
            if not isinstance(self._main_widget, PGERootWidget):
                raise TypeError('Main widget must be an instance of PGERootWidget')

            self._main_widget.surface = self.surface.subsurface(self._main_widget.rect)

    @property
    def main_widget(self):
        return self._main_widget

    @main_widget.setter
    def main_widget(self, new_widget):
        if not isinstance(new_widget, PGERootWidget):
            raise TypeError('Main widget must be an instance of PGERootWidget')

        self._main_widget = new_widget
        self._main_widget.surface = self.surface.subsurface(self._main_widget.rect)

    def paint(self):
        """ Handle painting this display and all of its widgets during the event loop.

            :return: None
        """
        if self._main_widget:
            self._main_widget.paint()

        pygame.display.flip()

    def _register_default_callbacks(self):
        """ Setup the default event signals and slots for this display.

            :return: None
        """
        Engine.instance().register_callback('paint', self.paint)
