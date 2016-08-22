""" Define the Display class, which manages the main window of the engine.
"""
import pygame

from pygame_engine.core.engine import Engine
from pygame_engine.lib.data import color


class Display(object):
    """ Represent a main display window for the PyGameEngine.
    """
    # TODO: Setup basic widgets such as buttons and labels.
    def __init__(self, size, main_widget=None, background_color=color.BLACK):
        self.main_widget = main_widget
        self.background_color = background_color
        self.surface = pygame.display.set_mode(size)
        self.size = size
        self._register_default_callbacks()

    def paint(self):
        """ Handle painting this display and all of its widgets during the event loop.

            :return: None
        """
        self.surface.fill(self.background_color)

        if self.main_widget:
            self.main_widget.blit()

    def _register_default_callbacks(self):
        """ Setup the default event signals and slots for this display.

            :return: None
        """
        Engine.instance().register_callback('paint', self.paint)
