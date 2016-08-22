""" Define the Display class, which manages the main window of the engine.

    Author: Ian Davis
"""
import pygame

from pygame_engine.core.engine import Engine


class Display(object):
    """ Represent a main display window for the PyGameEngine.
    """

    def __init__(self, size, main_widget=None):
        self._main_widget = main_widget
        self.surface = pygame.display.set_mode(size)
        self.size = size
        self._register_default_callbacks()

    @property
    def main_widget(self):
        return self._main_widget

    @main_widget.setter
    def main_widget(self, new_widget):
        self._main_widget = new_widget
        self._main_widget.surface = self.surface.subsurface()

    def paint(self):
        """ Handle painting this display and all of its widgets during the event loop.

            :return: None
        """
        if self._main_widget:
            self._main_widget.paint()

    def _register_default_callbacks(self):
        """ Setup the default event signals and slots for this display.

            :return: None
        """
        Engine.instance().register_callback('paint', self.paint)
